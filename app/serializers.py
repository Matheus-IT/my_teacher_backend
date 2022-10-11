from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import ScheduledClass, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class RegisterClassSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=100)

    def validate_name(self, name):
        if len(name) < 3:
            raise ValidationError('deve ter pelo menos três caracteres')
        return name


class ScheduledClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledClass
        fields = '__all__'
