from django.views.generic import TemplateView

class TeacherDashboardTemplateView(TemplateView):
    template_name = 'teachers/dashboard.html'