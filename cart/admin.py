from django.contrib import admin
from .models import Coupon, ShippingFee
# Register your models here.
admin.site.register(Coupon)
admin.site.register(ShippingFee)