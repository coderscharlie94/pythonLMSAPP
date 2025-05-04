from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .Serializers import StudentRegistrationSerializer, StudentLoginSerializer
class StudentRegisterAPIView(APIView):
   permission_classes=[AllowAny] 
   def post(self, request):
       serializer = StudentRegistrationSerializer(data=request.data)
       if serializer.is_valid():
           student = serializer.save()
           return Response({"message": "User is created successfully"}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class StudentLoginAPIView(APIView):
   permission_classes = []  # Allow public access
   def post(self, request):
       serializer = StudentLoginSerializer(data=request.data)
       if serializer.is_valid():
           return Response(serializer.validated_data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)