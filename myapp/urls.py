from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),

    path('services', views.services, name='services'),

    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
  #  path('login', views.login, name='login'),
]
