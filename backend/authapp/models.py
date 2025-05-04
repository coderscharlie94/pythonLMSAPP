from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from .UserRoles import UserRole
class Student(models.Model):
   fullName = models.CharField(max_length=100)
   emailId = models.CharField(max_length=100, unique=True)
   password = models.CharField(max_length=100)
   mobile = models.CharField(max_length=100)
   role=models.CharField(
       max_length=20,
       choices=UserRole.choices,
       default=UserRole.STUDENT,
       blank=True,
       null=True
   )
   created_at = models.DateTimeField(auto_now_add=True)
   
   def set_password(self, raw_password):
       self.password = make_password(raw_password)
       
   def check_password(self, raw_password):
       return check_password(raw_password, self.password)
   
   def __str__(self):
       return self.emailId