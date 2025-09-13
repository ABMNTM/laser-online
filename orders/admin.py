# from django.contrib import admin
# from .models import Order

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('receipt_code', 'full_name', 'mobile', 'status', 'cost', 'estimated_time', 'created_at')
#     list_filter = ('status',)
#     search_fields = ('receipt_code', 'full_name', 'mobile')
#     list_editable = ('status', 'cost', 'estimated_time')


from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['receipt_code', 'full_name', 'mobile', 'email', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['receipt_code', 'full_name', 'mobile', 'email']

admin.site.register(Order, OrderAdmin)
