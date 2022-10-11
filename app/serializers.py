from rest_framework import serializers
from .models import ScheduledClass, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class RegisterClassSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=100)


class ScheduledClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledClass
        fields = '__all__'
