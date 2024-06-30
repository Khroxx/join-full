from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TodoItem, JoinUser


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        #fields= ('title', 'created_at', 'description', 'priority', 'user', 'category', 'subtask', 'status')
        read_only_fields = ['username']
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password')
        
    def create(self, validated_data):
        user = JoinUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone']
        )
        return user
    
class JoinUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUser
        fields = '__all__'