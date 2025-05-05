from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, UserProfile
from .Serializers import CustomUserSerializer, UserProfileSerializer,CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class RegisterView(generics.CreateAPIView):
   permission_classes=[] 
   queryset = CustomUser.objects.all()
   serializer_class = CustomUserSerializer
   
class LoginView(TokenObtainPairView):
    permission_classes=[]
    serializer_class=CustomTokenObtainPairSerializer


class UserProfileListCreateView(generics.ListCreateAPIView):
   permission_classes=[IsAuthenticated] 
   queryset = UserProfile.objects.all()
   serializer_class = UserProfileSerializer
   permission_classes = [permissions.IsAuthenticated]
   def perform_create(self, serializer):
       serializer.save(user=self.request.user)
       
       
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
   permission_classes=[IsAuthenticated] 
   serializer_class = UserProfileSerializer
   permission_classes = [permissions.IsAuthenticated]
   def get_queryset(self):
       return UserProfile.objects.filter(user=self.request.user)