from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Student
class StudentRegistrationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Student
       fields = ['fullName', 'emailId', 'password', 'mobile','role']
       extra_kwargs = {'password': {'write_only': True}}
   def create(self, validated_data):
       role=validated_data.get('role') or 'student'
       if role is None and role is "":
           role=''
       student = Student(
           fullName=validated_data['fullName'],
           emailId=validated_data['emailId'],
           mobile=validated_data['mobile'],
           role=role
       )
       student.set_password(validated_data['password'])
       student.save()
       return student
        
class StudentLoginSerializer(serializers.Serializer):
   emailId = serializers.CharField()
   password = serializers.CharField(write_only=True)
   def validate(self, data):
       email = data.get('emailId')
       password = data.get('password')
       try:
           student = Student.objects.get(emailId=email)
       except Student.DoesNotExist:
           raise serializers.ValidationError("Invalid email or password")
       if not student.check_password(password):
           raise serializers.ValidationError("Invalid email or password")
       # Generate JWT tokens
       refresh = RefreshToken.for_user(student)
       return {
           'refresh': str(refresh),
           'access': str(refresh.access_token),
           'student': {
               'fullName': student.fullName,
               'emailId': student.emailId,
               'mobile': student.mobile,
               'role':student.role
           }
       }