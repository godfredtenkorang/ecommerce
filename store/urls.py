from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView


urlpatterns = [
    path('index/', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('about/', views.about, name='about-page'),
    # path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-info'),
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    path('product/<slug:homeproduct_slug>/', views.home_product_info, name='home-product-info'),
    path('product/<slug:slideproduct_slug>/', views.slide_product_info, name='slide-product-info'),
    # Individual category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
    
    # Review
    path('review/<int:product_id>/', views.review_rate, name='review'),
    path('review/<int:review_id>/', views.review_replies, name='review-reply'),
    
    # Contact
    
    path('contact/', views.contact, name='contact'),
    
    # Policy
    path('policy/', views.our_policy, name='our-policy'),
    
    # FAQ
    path('faq/', views.faq, name='faq'),
    
    path('our-story/', views.our_story, name='our-story'),
    

    path('news/', NewsListView.as_view(), name='our-news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='our-news-detail'),
    
    path('', views.under_construction, name='under-construction'),
    
]