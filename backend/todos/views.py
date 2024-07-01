from django.shortcuts import render
from django.views import generic
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import TodoItem, JoinUser, TodoSubtask
from .serializers import RegisterSerializer, TodoItemSerializer, JoinUserSerializer, SubtaskSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import viewsets, status

# Create your views here.


class JoinUserView(APIView):
    permission_classes = [AllowAny] # Keine Authentifizierung erforderlich
    def get(self, request, format=None):
        users = JoinUser.objects.all()
        serializer = JoinUserSerializer(users, many=True)
        return Response(serializer.data)

class TodoItemView(APIView):
    #authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny] # Keine Authentifizierung erforderlich
    
    def get(self, request, format=None):
        todos = TodoItem.objects.all()
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data)
    
class SubtaskView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, format=None):
        subtasks = TodoSubtask.objects.all()
        serializer = SubtaskSerializer(subtasks, many=True)
        return Response(serializer.data)
    

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class RegisterUserView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Benutzer erfolgreich registriert"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)