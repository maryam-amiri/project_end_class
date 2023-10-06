from django.urls import path

from . import views

#dar urls asli namespace tarif kardim pas:
app_name='home-module'

urlpatterns=[
    path('',views.home_func,name='home')
]