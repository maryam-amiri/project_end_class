from django.shortcuts import render

# Create your views here.

app_name='home_module'
def home_func(request):
    return render(request,'home_module/home_page.html')