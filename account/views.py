from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.
def register(request):

    return render(request, 'account/registration/register.html')