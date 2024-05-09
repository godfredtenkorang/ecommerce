from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('about/', views.about, name='about-page'),
    # path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-info'),
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    path('product/<slug:product_slug>/', views.home_product_info, name='home-product-info'),
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
    
]