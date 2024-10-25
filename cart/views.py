from django.shortcuts import render, redirect
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Coupon



def cart_summary(request):
    coupons = Coupon.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        if 'apply_coupon' in request.POST:
            coupon_code = request.POST.get('coupon_code')
            if cart.apply_coupon(coupon_code):
                messages.success(request, f'Coupon "{coupon_code}" applied succussfully!')
            else:
                messages.warning(request, f'Coupon "{coupon_code}" is not valid.')
            return redirect('cart-summary')
            
        elif 'remove_coupon' in request.POST:
            cart.remove_coupon()
            
    context = {
        'cart': cart,
        'title': 'Cart',
        'coupons': coupons
    }
    
    return render(request, 'cart/cart-summary.html', context)

def cart_add(request):
    
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product, product_qty=product_quantity)
        
        cart_quantity = cart.__len__()
        
        response = JsonResponse({'qty': cart_quantity})
        
        return response

def cart_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})
        return response
        

def cart_update(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        
        cart.update(product=product_id, qty=product_quantity)

        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        
        response = JsonResponse({'qty': cart_quantity, 'total': cart_total})
        return response
