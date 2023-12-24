from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default="un-branded")
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "products"
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
    
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = "contacts"
        
    def __str__(self):
        return self.full_name
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "reviews"
    
    def __str__(self):
        return self.user.username