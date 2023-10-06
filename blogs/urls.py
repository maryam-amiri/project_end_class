from django.contrib.auth import admin
from django.urls import path
from . import views

urlpatterns=[
    # path('',views.index,name='starting_page'),
    # path('posts',views.posts,name='post_page'),
    # path('posts/<slug:slug>',views.single_post,name='post_detail'),
    # path('k',views.karbaran_list),
    path('',views.product_list,name='product-list'),
    # path('<int:product_id>',views.product_details)
    path('<slug:slug>',views.product_details,name='product-details')
]
