from django.urls import path
from dayStarApp import views
from django.contrib.auth import views as auth_views

# app urls 
urlpatterns = [
    path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),

    # sitter urls
    path('sitter-reg/', views.sitterReg, name='sitter-reg'),
    path('sitters/', views.sitters, name='sitters'),
    path('details/<int:id>', views.viewSitter, name="details"),
    path('edit/<int:item_id>/', views.edit_page, name='edit_sitter'),
    path('delete/<int:id>/', views.deleteSitter, name="delete"),

    # baby urls
    path('babyreg/', views.babyReg, name='babyreg'),
    path('babies/', views.babys, name='babys'),
    # path('edit/<int:item_id>/', views.edit_baby, name='edit_baby'),
    path('delete/<int:id>/', views.deleteBaby, name="delete"),

    #payment urls
    path('payment/', views.payment, name='payment'),
    path('payment/sale/<int:id>', views.payment, name='payment'),

    #sales
    path('sale/', views.sale, name='sale'),
    path('sale/addstock/', views.addItem, name='addstock'),
    

    # admin logs urls
    path("login/", auth_views.LoginView.as_view(template_name='dayStarApp/login.html'), name="login"), 
    path('logout/', views.logout_view, name='logout'),
]
