from django.urls import path
from leave_request import views

app_name = "leave_request"

urlpatterns = [
    path('submit-leave/', views.submit_leave_request, name='submit-leave'),
    path('leave/<int:request_id>/', views.leave_request_detail, name='leave-request-detail'),
]