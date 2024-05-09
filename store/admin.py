from django.contrib import admin
from . models import Category, Product, Contact, Review, Home_Product, Slide_Product


# @admin.register(Category)
# class CategotyAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
    

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
    
class ProductInLine(admin.TabularInline):
    model = Product
    extra = 3
    
  
  
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name', 'slug']})]
    inlines = [ProductInLine]
  
admin.site.register(Category, CategoryAdmin)


admin.site.register(Home_Product)
admin.site.register(Slide_Product)
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'rate', 'comment', 'created_at']
    readonly_fields = ['created_at', ]

# admin.site.register(Review)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone',
                    'message']
    # readonly_fields = ['full_name', ]

# admin.site.register(Contact)