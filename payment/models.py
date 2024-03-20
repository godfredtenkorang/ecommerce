from django.db import models
from django.contrib.auth.models import User

from store.models import Product

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

DELIVERY = (
    ("INTERNATIONAL", "International"),
    ("DOMESTIC", "Domestic")
)

class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=300)
    email = models .EmailField(max_length=255)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    country = models.CharField(max_length=20, choices=CHOICES, default="GHANA")
    phone_number = models.CharField(max_length=20, default=0)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.CharField(max_length=50, choices=DELIVERY, default="International")
    
    
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
