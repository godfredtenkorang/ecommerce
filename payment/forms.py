from django import forms
from . models import ShippingAddress


class ShoppingForm(forms.ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'email', 'address1', 'address2', 'phone_number', 'country', 'city', 'state', 'zipcode', 'delivery']
        exclude = ['user',]