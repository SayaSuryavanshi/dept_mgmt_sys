from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from .import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-department/', views.add_department, name='add_department'),
    path('edit-department/<int:pk>/', views.edit_department, name='edit_department'),
    path('delete-department/<int:pk>/', views.delete_department, name='delete_department'),
    path('logout/', views.user_logout, name='logout'),

]
