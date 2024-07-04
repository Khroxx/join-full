from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TodoItem, JoinUser, TodoSubtask


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        #fields= ('title', 'created_at', 'description', 'priority', 'user', 'category', 'subtask', 'status')
        read_only_fields = ['username']
    
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoSubtask
        fields = '__all__'
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = JoinUser
        fields = ('email', 'username', 'password')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            # phone=validated_data['phone']
        )
        return user
    
class JoinUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUser
        fields = ('id', 'email', 'username', 'phone', 'password')
        # fields = '__all__'