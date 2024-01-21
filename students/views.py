from django.views.generic import TemplateView

class StudentDashboardTemplateView(TemplateView):
    template_name = "students/dashboard.html"