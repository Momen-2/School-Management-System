from django.urls import path
from students import views

app_name = 'students'

urlpatterns = [
    path('student-dashboard', views.StudentDashboardTemplateView.as_view(), name='dashboard')
]