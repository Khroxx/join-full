from rest_framework import serializers
from .models import TodoItem, TodoSubtask, CustomUser


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        read_only_fields = ['username']
    
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoSubtask
        fields = '__all__'
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'phone')
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            # phone=validated_data['phone']
            phone = ''
        )
        return user
            
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username',  'phone')
        
