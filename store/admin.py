from django.contrib import admin
from . models import Category, Product, Contact


@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Contact)