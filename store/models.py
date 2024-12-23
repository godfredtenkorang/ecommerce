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
    previous_price = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "products"
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
    
class HomeProduct(models.Model):
    category = models.ForeignKey(Category, related_name='homeproduct', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default="un-branded")
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50)
    previous_price = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images/home/")
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "home products"
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home-product-info', args=[self.slug])
    
class SlideProduct(models.Model):
    category = models.ForeignKey(Category, related_name='slideproduct', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default="un-branded")
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50)
    previous_price = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images/home/")
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Slide products"
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
    
# class ButterProduct(models.Model):
#     category = models.ForeignKey(Category, related_name='butterproduct', on_delete=models.CASCADE, null=True)
#     title = models.CharField(max_length=250)
#     brand = models.CharField(max_length=250, default="un-branded")
#     description = models.TextField(blank=True)
#     slug = models.SlugField(max_length=50)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#     image = models.ImageField(upload_to="images/home/")
#     date_added = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         verbose_name_plural = "Butter products"
        
#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse('product-info', args=[self.slug])
    
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=20)
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
        return self.product.title
    
class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.review.product.title}"
    
    
    
class News(models.Model):
    title1 = models.CharField(max_length=200)
    content1 = models.TextField()
    image1 = models.ImageField(upload_to='news/img/')
    title2 = models.CharField(max_length=200, null=True)
    content2 = models.TextField(null=True)
    image2 = models.ImageField(upload_to='news/img/', null=True)
    title3 = models.CharField(max_length=200, null=True)
    content3 = models.TextField(null=True)
    image3 = models.ImageField(upload_to='news/img/', null=True)
    title4 = models.CharField(max_length=200, null=True)
    content4 = models.TextField(null=True)
    image4 = models.ImageField(upload_to='news/img/', null=True)
    title5 = models.CharField(max_length=200, null=True)
    content5 = models.TextField(null=True)
    image5 = models.ImageField(upload_to='news/img/', null=True)
    slug = models.SlugField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-date_posted']
        
    def __str__(self):
        return self.title1
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username