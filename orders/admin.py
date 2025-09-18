from django.contrib import admin

from utils.email import send_email
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['receipt_code', 'full_name', 'mobile', 'email', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['receipt_code', 'full_name', 'mobile', 'email']

    def save_model(self, request, obj: Order, form, change):
        super().save_model(request, obj, form, change)

        if change:
            if obj.cost is not None and obj.estimated_time is not None:
                # create payment detail to pay cost
                dummy_link = "https://test.com/pay"
                send_email(obj.email, "customer_payment", obj, dummy_link)

admin.site.register(Order, OrderAdmin)
