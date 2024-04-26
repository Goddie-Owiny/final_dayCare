from django.urls import path
from dayStarApp import views


# app urls 
urlpatterns = [
    path('', views.index, name='index'),
    path('sitter/', views.sitter, name='sitter'),
]