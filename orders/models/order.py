from django.db import models
from utils.receipt_code import generate_receipt_code


class Order(models.Model):
    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"

    pend_of_admin = "PA"
    pend_of_payment = "PP"
    accepted = "AC"
    cancelled = "CL"

    ORDER_STATUS = (
        (pend_of_admin, "Pending of admin"),
        (pend_of_payment, "Pending of payment"),
        (accepted, "Accepted"),
        (cancelled, "Cancelled")
    )

    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)
    address = models.TextField()
    email = models.EmailField()
    cnc_file = models.FileField(upload_to='cnc_files/')
    material = models.CharField(max_length=100)
    thickness = models.CharField(max_length=10)
    receipt_code = models.CharField(max_length=8, unique=True, default=generate_receipt_code)
    created_at = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estimated_time = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=2, choices=ORDER_STATUS, default=pend_of_admin)

    def __str__(self):
        return f"Order {self.receipt_code} by {self.full_name}"
