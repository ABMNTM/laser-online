from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from orders.forms import OrderForm
from orders.models import Order
from laser_online_backend.settings import ADMIN_EMAIL

from utils.email import send_email

