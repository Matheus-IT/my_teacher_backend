from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.serializers import RegisterClassSerializer, ScheduledClassSerializer, TeacherSerializer
from .models import ScheduledClass, Teacher


class TeacherApiView(APIView):
    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterClassApiView(APIView):
    def post(self, request, teacher_id, format=None):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        register_serializer = RegisterClassSerializer(data=request.data)
        if register_serializer.is_valid():
            class_ = ScheduledClass.objects.create(
                name=register_serializer.validated_data['name'],
                email=register_serializer.validated_data['email'],
                teacher=teacher,
            )
            class_serializer = ScheduledClassSerializer(class_)
            return Response(class_serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                'message': 'houveram erros de validação',
                'errors': register_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )



