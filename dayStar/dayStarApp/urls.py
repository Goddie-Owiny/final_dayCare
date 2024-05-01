from django.urls import path
from dayStarApp import views
from django.contrib.auth import views as auth_views

# app urls 
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.index, name='home'),

    # sitter urls
    path('sitter/', views.sitter, name='sitter'),
    path('details/<int:id>', views.viewSitter, name="details"),
    path('delete/<int:id>/', views.deleteSitter, name="delete"),

    # baby urls
    path('baby/', views.baby, name='baby'),

    # supply urls
    path('supply/', views.supply, name='supply'),

    # admin logs urls
    path("login/", auth_views.LoginView.as_view(template_name='dayStarApp/login.html')), 
    path('logout/', views.logout_view, name='logout'),
]
