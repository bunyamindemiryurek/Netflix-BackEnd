from django.urls import path
from .views import *
 
urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/',userLogin, name='login'),
    path('profiles/', profiles, name='profiles'),
    path('create-profile/', create, name='create'),
    path('hesap/', hesap, name='hesap'),
    path('edit/', edit, name='edit'),
    path('changr/', change, name='change'),
    path('logout/', userLogout, name='logout')
] 