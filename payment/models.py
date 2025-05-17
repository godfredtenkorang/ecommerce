from django.db import models
from django.contrib.auth.models import User

from store.models import Product
from .paystack import PayStack
import secrets

CHOICES = (
    ("ALGERIA", "Algeria"),
    ("ANGOLA", "Angola"),
    ("ARGENTINA", "Angentina"),
    ("AUSTRALIA", "Australia"),
    ("BELGIUM", "Belgium"),
    ("BRAZIL", "Brazil"),
    ("BURKINA FASO", "Burkina Faso"),
    ("CANADA", "Canada"),
    ("DENMARK", "Denmark"),
    ("GHANA", "Ghana"),
    
)


class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=300)
    email = models .EmailField(max_length=255)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, null=True)
    country = models.CharField(max_length=20, choices=CHOICES, default="GHANA")
    phone_number = models.CharField(max_length=20, default=0)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Shipping Address'
        
    def __str__(self):
        return 'Shipping Address - ' + str(self.id)


class Order(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=255)
    shipping_address = models.TextField(max_length=10000)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return "Order - #" + str(self.id)

CHOICES = (
    ('Delivered', 'Delivered'),
    ('Not delivered', 'Not delivered'),
)
 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    delivered = models.CharField(max_length=50, choices=CHOICES, default="Not delivered")
    
    def __str__(self):
        return "Order Item - #" + str(self.id)



class Payment(models.Model):
    full_name = models.CharField(max_length=300, default="")
    email = models .EmailField(max_length=255, default="")
    address = models.CharField(max_length=300, default="")
    phone_number = models.CharField(max_length=20, default=0)
    country = models.CharField(max_length=20, default="Ghana")
    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveBigIntegerField(default=0)
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Payments'
        
    def __str__(self) -> str:
        return f"Payment: {self.amount}"
    
    def amount_in_kobo(self):
        """Convert amount to kobo (Paystack requires amount in kobo)"""
        return int(self.amount * 100)
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
        
    def amount_value(self) -> int:
        return self.amount * 101
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 101 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False