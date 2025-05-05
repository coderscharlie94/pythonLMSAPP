from rest_framework import serializers
from .models import CustomUser, UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class CustomUserSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True)
   class Meta:
       model = CustomUser
       fields = ['id', 'email', 'name', 'password']
   def create(self, validated_data):
       return CustomUser.objects.create_user(**validated_data)
class UserProfileSerializer(serializers.ModelSerializer):
   user = CustomUserSerializer(read_only=True)
   class Meta:
       model = UserProfile
       fields = '__all__'
       
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token=super().get_token(user)
        token['email']=user.email
        token['name']=user.name
        return token