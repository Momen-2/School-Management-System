from django.views.generic import TemplateView

class AdminDashboardTemplateView(TemplateView):
    template_name = 'admins/dashboard.html'