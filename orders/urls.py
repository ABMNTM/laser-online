from django.urls import path
from orders import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('track/<str:receipt_code>/', views.track_order, name='track_order'),
]