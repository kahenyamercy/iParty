from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),  # List events
    path('create/', views.event_create, name='event_create'),  # Create new event
    path('<int:pk>/', views.event_detail, name='event_details'),  # Event detail
    path('<int:pk>/update/', views.event_update, name='event_update'),  # Update event
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),  # Delete event
    path('<int:pk>/register/', views.register_for_event, name='register_for_event'),  # Register for event
]
