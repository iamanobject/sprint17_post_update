from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_users, name='users'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update', views.update_user.as_view(), name='update'),
    path('<int:pk>/delete', views.delete_user.as_view(), name='delete'),
]