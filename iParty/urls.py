from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('campus/', include('campus.urls')),
    path('bookings/', include('bookings.urls')),
    path('events/', include('events.urls')),
    path('transactions/', include('transactions.urls')),
    path('', include('app.urls')),
]
