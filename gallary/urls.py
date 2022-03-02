from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from.import views

from gallary.views import demo_rest
from rest_framework import routers,serializers,viewsets

router = routers.DefaultRouter()
router.register(r'users',demo_rest,basename='MyModel')

urlpatterns = [
    path('',views.home,name='home'),
    path('second',views.second,name='second'),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('cart',views.cart,name="cart"),
    path('order',views.orderd,name="order"),
    path('checout',views.checkout,name="checkout"),
    path('user',views.user,name="user"),
    path('api',include(router.urls)),
    path('api_auth/',include('rest_framework.urls',namespace='rest_framework')),
]