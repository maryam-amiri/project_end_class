from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'enter email'}))
    first_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please username'}))
    last_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please username'}))
    password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please password'}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please repeat password'}))
    #---------------------------------------------function of validation:baraye tamame ebarate bala clean_ minevisim va unique boodan baraye username va email minavisim/har formi baraye neveshtane etebar sanji dar haman class minevisim
    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exist')
        return user

    #asamie samte chap dar model bayad vojood dashte bashad.
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exist')
        return email

    #--------2 ta moteghayer bayad tarif konim k har do password ra moghayese konim
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1!=password2:
            raise forms.ValidationError('password not match')
        elif len(password2)<8:
            raise forms.ValidationError('password is too short')
        #------hadaghal yek harfe bozorg:
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('upper letter use please')
        return password2

#-------------------------------class login

class UserLoginForm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()