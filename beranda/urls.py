from django.urls import path

from . import views

urlpatterns = [
    path('', views.beranda),
    path('beranda/', views.index),

]