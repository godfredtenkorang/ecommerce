from django.urls import path
from . import views

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('guest-checkout/', views.guest_checkout, name='guest-checkout'),
    path('complete-order', views.complete_order, name='complete-order'),
    path('set_shipping', views.set_shipping, name='set-shipping'),
    path('payment-success', views.payment_success, name='payment-success'),
    path('payment-failed', views.payment_failed, name='payment-failed'),
    path('make_payment/<str:ref>/', views.verify_payment, name='verify-payment'),
]