from django.shortcuts import render

# Create your views here.
def my_dashboard(request):
    return render(request, 'dashboard/my-dashboard.html')