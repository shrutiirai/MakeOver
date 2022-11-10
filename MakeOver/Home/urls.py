from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('login', views.login, name='login')
]
