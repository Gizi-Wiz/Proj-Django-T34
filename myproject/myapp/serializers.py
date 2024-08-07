from rest_framework import serializers
from .models import UserProfile, List, Task

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = List
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'