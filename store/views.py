from django.shortcuts import render
from . models import Category, Product, Contact
from django.shortcuts import get_object_or_404
from django.db.models import Q # New

# Create your views here.
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


def categories(request):
    
    all_categories = Category.objects.all()
    
    return {'all_categories': all_categories}

def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/list-category.html', {'category':category, 'products':products})


def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, 'store/product-info.html', context)

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(full_name=full_name, email=email, message=message)
        contact.save()
        return render(request, 'store/contact.html')
        
    return render(request, 'store/contact.html', {'title': 'Contact'})