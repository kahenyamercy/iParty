from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('detail/<int:pk>/', views.user_detail, name='user_detail'),
    path('create/', views.user_create, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('update/<int:pk>/', views.user_update, name='user_update'),
    path('delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('logout/', views.user_logout, name='user_logout'),
]
