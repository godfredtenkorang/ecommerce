from django.shortcuts import get_object_or_404, render, redirect
from .models import Payment, ShippingAddress, Order, OrderItem
from cart.cart import Cart
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from cart.models import ShippingFee
from django.contrib import messages

from django.db import transaction
from django.contrib.auth.decorators import login_required

# Create your views here.

def checkout(request):
    cart = Cart(request)
    
    total_price = cart.get_all_total()
    
    user = request.user
    
    # Handle shipping fee selection
    if request.method == 'POST' and 'set_shipping' in request.POST:
        country_id = request.POST.get('country_id')
        if country_id:
            if cart.set_shipping_fee(country_id):
                messages.success(request, "Shipping fee updated")
            else:
                messages.error(request, "Invalid shipping country selected")
        return redirect('checkout')
    
    # Users with addounts -- Pro-fill the form
    
    if request.method == 'POST':
        
        try:
            full_name = request.POST.get('full_name')
            if not full_name:
                raise ValueError("Full name is required")
            email = request.POST.get('email')
            if not email:
                raise ValueError("Email is required")
            address = request.POST.get('address1')
            if not address:
                raise ValueError("Address is required")
            phone_number = request.POST.get('phone_number')
            if not phone_number:
                raise ValueError("Phone number is required")
            country = request.POST.get('country')
            if not country:
                raise ValueError("Country is required")
            city = request.POST.get('city')
            if not city:
                raise ValueError("City is required")
            state = request.POST.get('state', '')
            zipcode = request.POST.get('zipcode', '')
            
            payment = Payment(
                full_name=full_name, 
                email=email, 
                address=address, 
                phone_number=phone_number, 
                country=country, city=city, 
                state=state, 
                zipcode=zipcode, 
                user=user if user.is_authenticated else None,
                amount=total_price
            )
            payment.save()
            
            return render(request, 'payment/make_payment.html', {
                'cart': cart, 
                'title': 'Cart', 
                'payment': payment, 
                'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
            })
        
        except Exception as e:
            # Handle form errors
            messages.error(request, f"There was an error processing your order: {str(e)}")
            return redirect('checkout')
    
    # GET request handling
    shipping_address = None
    selected_country_id = cart.get_shipping_country_id()
    
    if request.user.is_authenticated:
        try:
            shipping_address = ShippingAddress.objects.get(user=request.user)
            if not selected_country_id:  # Use user's default country if none selected
                selected_country_id = shipping_address.country
        except ShippingAddress.DoesNotExist:
            pass
            
    context = {
        'shipping': shipping_address,
        'cart': cart,
        'title': 'Cart',
        'shipping_fees': ShippingFee.objects.all(),
        'selected_country_id': selected_country_id,
        'shipping_fee': cart.get_shipping_fee(),
        'subtotal': cart.get_total(),
        'total': cart.get_all_total()
    }
    return render(request, 'payment/checkout.html', context=context)
            
            
def set_shipping(request):
    if request.method == 'POST':
        # Check for AJAX request (modern way)
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        if is_ajax:
            cart = Cart(request)
            country_id = request.POST.get('country_id')
            if country_id:
                cart.set_shipping_fee(country_id)
                return JsonResponse({
                    'shipping_fee': cart.get_shipping_fee(),
                    'total_price': cart.get_all_total()
                })
        return JsonResponse({'error': 'Invalid request'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def guest_checkout(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Validate required fields
                required_fields = {
                    'full_name': "Full name is required",
                    'email': "Email is required",
                    'address1': "Shipping address is required",
                    'country': "Country is required",
                    'phone_number': "Phone number is required",
                    'city': "City is required"
                }
                
                data = {}
                for field, error_msg in required_fields.items():
                    value = request.POST.get(field)
                    if not value:
                        raise ValueError(error_msg)
                    data[field] = value

                # Additional optional fields
                data['address2'] = request.POST.get('address2', '')
                data['state'] = request.POST.get('state', '')
                data['zipcode'] = request.POST.get('zipcode', '')

                # Create shipping address
                shipping_address = f"""
                {data['full_name']}
                {data['address1']}
                {data['address2'] if data['address2'] else ''}
                {data['city']}, {data['state']} {data['zipcode']}
                {data['country']}
                Phone: {data['phone_number']}
                """.strip()

                # Get cart
                cart = Cart(request)
                if not cart:
                    raise ValueError("Your cart is empty")

                total_cost = cart.get_all_total()

                # Create order (no user association)
                order = Order.objects.create(
                    full_name=data['full_name'],
                    email=data['email'],
                    shipping_address=shipping_address,
                    amount_paid=total_cost
                )

                # Create order items
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        quantity=item['qty'],
                        price=item['price']
                    )

                # Send confirmation email
                product_list = [item['product'].title for item in cart]
                email_body = f"""
                Order Confirmation #{order.id}
                --------------------------
                Customer: {data['full_name']}
                Email: {data['email']}
                
                Products:
                {', '.join(product_list)}
                
                Total: ${total_cost}
                
                Shipping Address:
                {shipping_address}
                
                Note: This is a guest order
                """

                send_mail(
                    f'Your Order #{order.id}',
                    email_body,
                    [data['email']],
                    [data['email']],
                    fail_silently=False
                )

                # Clear cart
                cart.clear()

                return JsonResponse({
                    'success': True,
                    'order_id': order.id,
                    
                })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)

    return render(request, 'checkout/guest_checkout.html')
    

@login_required(login_url='/accounts/my-login')  # Require login for all orders
def complete_order(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                name = request.POST.get('full_name', request.user.get_full_name())
                email = request.POST.get('email', request.user.email)
                address1 = request.POST.get('address1')
                address2 = request.POST.get('address2', '')
                country = request.POST.get('country')
                phone_number = request.POST.get('phone_number')
                city = request.POST.get('city')
                state = request.POST.get('state', '')
                zipcode = request.POST.get('zipcode', '')
                
                # All-in-one shipping address
                
                # Validate required fields
                required_fields = {
                    'address1': "Shipping address is required",
                    'country': "Country is required",
                    'phone_number': "Phone number is required",
                    'city': "City is required"
                }
                
                for field, error_msg in required_fields.items():
                    if not request.POST.get(field):
                        raise ValueError(error_msg)
                
                # Create shipping address
                shipping_address = f"""
                {name}
                {address1}
                {address2 if address2 else ''}
                {city}, {state} {zipcode}
                {country}
                Phone: {phone_number}
                """.strip()
                
                # Get cart and validate
                cart = Cart(request)
                
                if not cart:
                    raise ValueError("Your cart is empty")
               
                # Get the total price of items
                
                total_cost = cart.get_all_total()
                
                '''
                    Order variations
                    
                    1) Create order -> Account users WITH + WITHOUT shipping information
                    
                    2) Create order -> Guest users without an account
                    
                '''
                # 1) Create order -> Account users WITH + WITHOUT shipping information
                
                # Create order - always associated with logged-in user
                order = Order.objects.create(
                    user=request.user,
                    full_name=name,
                    email=email,
                    shipping_address=shipping_address,
                    amount_paid=total_cost
                )
                
                
                for item in cart:
                    OrderItem.objects.create(
                        order=order, 
                        product=item['product'], 
                        quantity=item['qty'], 
                        price=item['price'], 
                        user=request.user
                    )
                
            
            #     product_list = [item['product'].title for item in cart]
                
            #     email_body = f"""
            #         Order Confirmation #{order.id}
            #         --------------------------
            #         Customer: {name}
            #         Email: {email}
                    
            #         Products:
            #         {', '.join(product_list)}
                    
            #         Total: GH¢{total_cost}
                    
            #         Shipping Address:
            #         {shipping_address}
            #     """
            
                
            #     send_mail('Order received', email_body, settings.EMAIL_HOST_USER, [email], fail_silently=False,)
            #     send_mail(
            #     f"New Order #{order.id}",
            #     email_body,
            #     email,  # From email
            #     [settings.EMAIL_HOST_USER],  # To email
            #     fail_silently=False,
            # ),
            return JsonResponse({
                    'success': True,
                    'order_id': order.id,
                    
                })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)



    

def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        
        return redirect('payment-success')
    else:
        return redirect('payment-failed')



def payment_success(request):
    
    # Clear shopping cart
    
    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
    
    return render(request, 'payment/payment-success.html', {'title':"Payment successful"})


def payment_failed(request):

    return render(request, 'payment/payment-failed.html', {'title': "Payment failed"})


