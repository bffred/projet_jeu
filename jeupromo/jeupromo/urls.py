from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^games/', include('games.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns