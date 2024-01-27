from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('about/', views.about, name='about-page'),
    # path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-info'),
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    # Individual category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    
    # Review
    path('review/<int:product_id>/', views.review_rate, name='review'),
    
    # Contact
    
    path('contact/', views.contact, name='contact'),
    
    # Policy
    path('policy/', views.our_policy, name='our-policy'),
    
    # FAQ
    path('faq/', views.faq, name='faq'),
    
    # Wishlist
    

    # Added to wishlist
    
    path('add_to_wishlist/<int:product_id>/',
         views.add_to_wishlist, name='add-to-wishlist'),
    path('remove_from_wishlist/<slug:product_slug>/',
         views.remove_from_wishlist, name='remove-from-wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    
]