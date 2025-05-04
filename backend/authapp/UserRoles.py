# authapp/enums/roles.py
from django.db import models
class UserRole(models.TextChoices):
   STUDENT = 'student', 'Student'
   LIBRARIAN = 'librarian', 'Librarian'