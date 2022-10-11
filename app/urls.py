from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.TeacherApiView.as_view()),
    path('class/<str:teacher_id>/', views.RegisterClassApiView.as_view()),
]