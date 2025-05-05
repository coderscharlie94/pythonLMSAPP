from rest_framework import serializers
from .models import Student
class StudentRegistrationSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True)
   class Meta:
       model = Student
       fields = ['fullName', 'emailId', 'mobile', 'password']
   def create(self, validated_data):
       user = Student.objects.create_user(
           emailId=validated_data['emailId'],
           password=validated_data['password'],
           fullName=validated_data['fullName'],
           mobile=validated_data['mobile']
       )
       return user