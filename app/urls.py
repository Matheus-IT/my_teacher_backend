from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.TeacherApiView.as_view()),
]