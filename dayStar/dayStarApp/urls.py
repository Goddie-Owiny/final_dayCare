from django.urls import path
from dayStarApp import views
from django.contrib.auth import views as auth_views

# app urls 
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.index, name='home'),

    # sitter urls
    path('sitter-reg/', views.sitterReg, name='sitter-reg'),
    path('sitters/', views.sitters, name='sitters'),
    path('details/<int:id>', views.viewSitter, name="details"),
     path('edit/<int:item_id>/', views.edit_page, name='edit_sitter'),
    path('delete/<int:id>/', views.deleteSitter, name="delete"),

    # baby urls
    path('babyreg/', views.babyRegistration, name='baby'),
    path('babies/', views.babys, name='babys'),

    #supply urls
    path('supply/', views.supply, name='supply'),
    path('supply/sale/<int:id>', views.supply, name='supply'),
    

    # admin logs urls
    path("login/", auth_views.LoginView.as_view(template_name='dayStarApp/login.html')), 
    path('logout/', views.logout_view, name='logout'),
]
