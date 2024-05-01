from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('profile/', views.profilePage, name='profile'),
    path('edit-profile/', views.editProfilePage, name='edit-profile')
]