from django.urls import path
from . import views

app_name = 'campus'

urlpatterns = [
    path('', views.campus_list, name='campus_list'),
    path('<int:pk>/', views.campus_detail, name='campus_detail'),
    path('create/', views.campus_create, name='campus_create'),
    path('<int:pk>/update/', views.campus_update, name='campus_update'),
    path('<int:pk>/delete/', views.campus_delete, name='campus_delete'),
]
