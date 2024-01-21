from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("accounts.urls")),
    path("", include("admins.urls")),
    path("", include("classes.urls")),
    path("", include("courses.urls")),
    path("", include("home.urls")),
    path("", include("leave_request.urls")),
    path("", include("students.urls")),
    path("", include("subjects.urls")),
    path("", include("teachers.urls")),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)