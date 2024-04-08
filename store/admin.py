from django.contrib import admin
from . models import Category, Product, Contact, Review, WishList


@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'rate', 'comment', 'created_at']
    readonly_fields = ['created_at', ]

# admin.site.register(Review)

# admin.site.register(WishList)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone',
                    'message']
    # readonly_fields = ['full_name', ]

# admin.site.register(Contact)