from django.urls import path
from dayStarApp import views


# app urls 
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.index, name='index'),
    path('sitter/', views.sitter, name='sitter'),
    path('baby/', views.baby, name='baby'),
]
