from django.shortcuts import render, redirect
from . models import Category, Product, Contact, Review, Home_Product, Slide_Product
from django.shortcuts import get_object_or_404
from django.db.models import Q # New
# from django.views.generic import DetailView
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.urls import reverse

def index(request):
    home_products = Home_Product.objects.all()
    slide_products = Slide_Product.objects.all()
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(full_name=full_name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your form has been submitted")
        return render(request, 'store/index.html')
    context = {
        'home_products': home_products,
        'slide_products': slide_products
    }
    return render(request, 'store/index.html', context)


def store(request):
    search_item = request.GET.get('search')
    
    if search_item:
        all_products = Product.objects.filter(Q(title__icontains=search_item))
        
    else:
        all_products = Product.objects.all().order_by('date_added')
    context = {
        'all_products': all_products
    }
    return render(request, 'store/store.html', context)

def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'store/about.html', context)


def categories(request):
    
    all_categories = Category.objects.all()
    
    return {'all_categories': all_categories}

def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/list-category.html', {'category':category, 'products':products})


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "store/product-info.html"
#     slug_field = "slug"
#     count_hit = True
    
#     form = forms.ReviewForm
    
#     def product(self, request, *args, **kwargs):
#         form = forms.ReviewForm(request.POST)
#         if form.is_valid():
#             myproduct = self.get_object()
#             form.instance.user = request.user
#             form.instance.product = myproduct
#             form.save()
            
#             return redirect(reverse("product-info", kwargs={
#                 'slug': myproduct.slug
#             }))
            
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = self.form
#         return context
            
        
     
    
def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    try:
        # product_review = Product.objects.get(slug=product_slug)
        reviews = Review.objects.filter(product=product)
        review_counts = Review.objects.all().filter(product=product).count()
    except:
        return redirect('product-info')
    context = {
        'product': product,
        'reviews': reviews,
        'review_counts': review_counts,
        'title': 'product info'
    }
    return render(request, 'store/product-info.html', context)

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(full_name=full_name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your form has been submitted")
        return render(request, 'store/contact.html')
        
    return render(request, 'store/contact.html', {'title': 'Contact'})


def review_rate(request, product_id):
    if request.method == "POST":
        url = request.META.get('HTTP_REFERER')
        try:
            reviews = Review.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, "Thank you! Your review has been updated")
            return redirect(url)
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Review()
                data.comment = form.cleaned_data['comment']
                data.rate = form.cleaned_data['rate']
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(
                    request, "Thank you! Your review has been submitted")
                return redirect(url)
        # prod_slug = request.GET.get('prod_slug')
        # myproduct = Product.objects.get(slug=prod_slug)
        # comment = request.POST('comment')
        # rate = request.POST('rate')
        # user = request.user
        # review = Review(user=user, product=myproduct, comment=comment, rate=rate)
        # review.save()
        # return redirect('product-info', slug=prod_slug)
        

def our_policy(request):
    context = {
        'title': 'Our Policy'
    }
    return render(request, 'store/policy.html', context)

def faq(request):
    context = {
        'title': 'FAQ'
    }
    return render(request, 'store/faq.html', context)


def error_404(request, exception):
    return render(request, 'store/404.html')
