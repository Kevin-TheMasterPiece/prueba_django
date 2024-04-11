from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('otro/', views.otro),
    path('casco/', views.casco),
    path('hola/', views.hola), 
    path('hola/poque/', views.poque),
    path('hola/poque/nose', views.nose)
]
