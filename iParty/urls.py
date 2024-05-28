from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('campus/', include('campus.urls', namespace='campus')),
    path('bookings/', include('bookings.urls', namespace='bookings')),
    path('events/', include('events.urls', namespace='events')),
    path('transactions/', include('transactions.urls', namespace='transactions')),
    path('', include('app.urls', namespace='app')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
