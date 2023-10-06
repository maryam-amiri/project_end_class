from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
#az modele estefade shode dar auth django mikhahim estefade konim:
from django.contrib.auth.models import User
# Create your views here.

def contactus_func(request):
   return render(request,'contactus_module/contactus_page.html')

def user_register(request):
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        # etelaate tamiz ra befrestad:
        if form_register.is_valid():
            data = form_register.cleaned_data
            User.objects.create_user(username=data['user_name'],
                                     email=data['email'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     password=data['password2'])
            return redirect('home_module:home')
            # dar bala username az jadvale auth_user va user_name az forms va fieldhaye tarif shode amade
        # agar post nabashad method get ast:
    else:
        # obj az jense class tarif mikonim ta b azaye class dastresi dashte basham(class dar file forms)
        form_register = UserRegisterForm()
        # dar html besoorate dic tarif mishavad
    return render(request, 'contactus_module/register.html', {'form_register': form_register})

#----------------------------function login
def user_login(request):
    if request.method=='POST':
        form_login=UserLoginForm(request.POST)
        if form_login.is_valid():
            data=form_login.cleaned_data
            #------------------------------------etebar sanji login(vojood darad ya na/dorost vared mikonad)/user sabz rang marboot b forms
            #aval ba email vared sho age nashod user/tebghe pishfarz bar asase user name login mishavad alan mikhaym ba email(aval email peida kon ba name oun karbar vared sho
            try:
                user=authenticate(request,username=User.objects.get(email=data['user']),password=data['password'])
            except:
                user=authenticate(request,username=data['user'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('home_module:home')
    else:
        form_login=UserLoginForm()
    return render(request,'contactus_module/login.html',{'form_login':form_login})

#--------------------------------logout
def user_logout(request):
    logout(request)
    return redirect('home_module:home')