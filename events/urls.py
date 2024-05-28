from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('my-events/', views.event_list, name='user_events'),
    path('create/', views.create_event, name='create_event'),
    path('<int:pk>/', views.event_detail, name='event_details'),
    path('<int:pk>/update/', views.event_update, name='event_update'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('<int:pk>/register/', views.register_for_event, name='register_for_event'),
]
