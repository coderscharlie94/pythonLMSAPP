from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .Serializers import StudentRegistrationSerializer
from .models import Student
class RegisterView(APIView):
   permission_classes=[]
   def post(self, request):
       serializer = StudentRegistrationSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response({'message': 'Registration successful!'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
   permission_classes=[]
   def post(self, request):
       emailId = request.data.get('emailId')
       password = request.data.get('password')
       if not emailId or not password:
           return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
       user = authenticate(request, username=emailId, password=password)
       if user is not None:
           auth_login(request, user)
           return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
       else:
           return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)