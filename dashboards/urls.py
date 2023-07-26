from django.urls import path
from dashboards import views

app_name = 'dashboards'

urlpatterns = [
    path('admin-dashboard', views.AdminDashboardTemplateView.as_view(), name='admin-dashboard'),
    path('teacher-dashboard', views.TeacherDashboardTemplateView.as_view(), name='teacher-dashboard'),
    path('student-dashboard', views.StudentDashboardTemplateView.as_view(), name='student-dashboard')
]