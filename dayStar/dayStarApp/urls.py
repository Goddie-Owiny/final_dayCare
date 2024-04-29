from django.urls import path
from dayStarApp import views
from django.contrib.auth import views as auth_views

# app urls 
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.index, name='index'),
    path('sitter/', views.sitter, name='sitter'),
    path('baby/', views.baby, name='baby'),
    path('supply/', views.supply, name='supply'),

    path("login/", auth_views.LoginView.as_view(template_name='dayStarApp/login.html')), 
]
