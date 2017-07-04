from .utils import DefaultModelSerializer

import debug_toolbar
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


# Routing
urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^draceditor/', include('draceditor.urls')),
    url(r'^api/auth/auth$', obtain_jwt_token, name='get_token'),
    url(r'^api/auth/refresh$', refresh_jwt_token, name='refresh_token'),
    url(r'^api/auth/check$', verify_jwt_token, name='check_token'),
] + DefaultModelSerializer().urls()

try:
    urlpatterns = [url(r'^', include(settings.PROJECT_URLCONF))] + urlpatterns
except AttributeError:
    pass

if settings.DEBUG:
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]