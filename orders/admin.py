from django.contrib import admin
from django.urls import reverse

from utils.email import send_email
from orders.models import Order, Transaction


class OrderAdmin(admin.ModelAdmin):
    list_display = ['receipt_code', 'full_name', 'mobile', 'email', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['receipt_code', 'full_name', 'mobile', 'email']

    def save_model(self, request, obj: Order, form, change):
        super().save_model(request, obj, form, change)

        # if change:
        #     if obj.cost is not None and obj.estimated_time is not None:
        #         authority = get_authority(request, obj)
        #         transaction = Transaction.objects.create(
        #             order=obj,
        #             authority=authority,
        #         )
        #         callback_url = request.build_absolute_uri(reverse("verify"))
        #         send_email(obj.email, "customer_payment", obj, transaction.get_payment_url(callback_url))

admin.site.register(Order, OrderAdmin)
