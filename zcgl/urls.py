from django.contrib import admin
from django.urls import path, include

from apps.servers.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('users/', include('apps.users.urls', namespace='users')),
    path('servers/', include('apps.servers.urls', namespace='servers')),
]
