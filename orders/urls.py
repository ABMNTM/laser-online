from django.urls import path
from orders.views import orders, payment

urlpatterns = [
    path('', orders.index, name='index'),
    path('submit_order/', orders.submit_order, name='submit_order'),
    path('track/<str:receipt_code>/', orders.track_order, name='track_order'),
    path('verify/', orders.verify, name='verify')
]