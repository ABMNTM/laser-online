from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from orders.forms import OrderForm
from orders.models import Order
from laser_online_backend.settings import ADMIN_EMAIL

from utils.email import send_email


def index(request):
    return render(request, 'orders/index.html')

def submit_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            send_email(ADMIN_EMAIL, "admin_alert", order)
            return JsonResponse({
                'success': True,
                'order_id': order.id,
                'receipt_code': order.receipt_code
            })
        else:
            errors = {field: [error for error in errors] for field, errors in form.errors.items()}
            return JsonResponse({
                'success': False,
                'errors': errors
            }, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

def track_order(request, receipt_code):
    order = get_object_or_404(Order, receipt_code=receipt_code)
    return render(request, 'orders/track.html', {'order': order})

def verify(request):
    success = request.GET.get("success")
    return render(request, "orders/verify.html", {"payment_success": success})
