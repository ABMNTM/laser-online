from django.db import models
from django.utils import timezone

from laser_online_backend.settings import ZARINPAL_MERCHANT_ID

from orders.models import Order


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار پرداخت'),
        ('success', 'پرداخت موفق'),
        ('failed', 'پرداخت ناموفق'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سفارش", null=True, blank=True)
    authority = models.CharField(max_length=50, unique=True, verbose_name="کد اختصاصی زرین‌پال", blank=True, null=True)
    ref_id = models.CharField(max_length=50, verbose_name="کد پیگیری", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="وضعیت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    paid_at = models.DateTimeField(verbose_name="تاریخ پرداخت", blank=True, null=True)

    class Meta:
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش‌ها"
        ordering = ['-created_at']

    def __str__(self):
        return f"تراکنش {self.id} - {self.get_status_display()} - {self.amount} تومان"

    def get_payment_url(self, callback_url):
        """
        ایجاد لینک پرداخت با استفاده از SDK زرین‌پال
        """
        from zarinpal import Zarinpal
        zp = Zarinpal(ZARINPAL_MERCHANT_ID)
        result = zp.payments.request(
            amount=self.amount,
            description=self.description or "پرداخت سفارش",
            email=self.order.email,
            mobile=self.order.mobile,
            callback_url=callback_url
        )

        if result.get('status') == 100:
            self.authority = result['authority']
            self.save()
            return zp.generate_payment_url(result['authority'])
        else:
            raise Exception(f"خطا در ایجاد تراکنش: {result.get('message')}")

    def verify_payment(self, merchant_id):
        """
        تایید پرداخت از طریق زرین‌پال
        """
        from zarinpal import Zarinpal

        zp = Zarinpal(merchant_id)
        result = zp.payment_verification(
            amount=self.amount,
            authority=self.authority
        )

        if result.get('status') == 100:
            self.status = 'success'
            self.ref_id = result.get('ref_id')
            self.paid_at = timezone.now()
            self.save()
            return True, result
        else:
            self.status = 'failed'
            self.save()
            return False, result
