from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from .UserRoles import UserRole

class StudentManager(BaseUserManager):
    def create_user(self, emailId, password=None, **extra_fields):
        if not emailId:
            raise ValueError('Email is required')
        emailId = self.normalize_email(emailId)
        student = self.model(emailId=emailId, **extra_fields)
        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_superuser(self, emailId, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(emailId, password, **extra_fields)

class Student(AbstractBaseUser, PermissionsMixin):
    fullName = models.CharField(max_length=100)
    emailId = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.STUDENT,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='student_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='student_permissions')

    USERNAME_FIELD = 'emailId'
    REQUIRED_FIELDS = []

    objects = StudentManager()

    def __str__(self):
        return self.emailId
