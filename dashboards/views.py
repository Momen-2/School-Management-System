from django.views.generic import TemplateView

class AdminDashboardTemplateView(TemplateView):
    template_name = 'dashboards/admin-dashboard.html'
    
class TeacherDashboardTemplateView(TemplateView):
    template_name = 'dashboards/teacher-dashboard.html'
    
class StudentDashboardTemplateView(TemplateView):
    template_name = 'dashboards/student-dashboard.html'