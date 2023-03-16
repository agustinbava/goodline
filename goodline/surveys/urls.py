from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contactus/', views.contactus, name="contactus"),
    path('thanks/', views.thanks, name='thanks'),
]
