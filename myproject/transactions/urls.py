from django.urls import path
from . import views

app_name = 'transactions'  # Replace with your app's name

urlpatterns = [
    path('<int:pk>/', views.transaction_detail, name='transaction_detail'),  # Transaction detail
]
