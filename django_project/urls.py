import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('courses.urls', namespace='courses')),
    path('', include('dashboards.urls', namespace='dashboards')),
    path('', include('subjects.urls', namespace='subjects')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)