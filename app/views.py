from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.serializers import TeacherSerializer
from .models import Teacher

class TeacherApiView(APIView):
    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
