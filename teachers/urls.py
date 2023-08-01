from django.urls import path
from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('teacher-dashboard', views.TeacherDashboardTemplateView.as_view(), name='dashboard'),
]