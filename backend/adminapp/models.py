from django.db import models

# Create your models here.
class Book(models.Model):
    bookName=models.CharField(max_length=255)
    bookAuthor=models.CharField(max_length=255)
    bookPrice=models.IntegerField()
    
    def __str__(self):
       return self.bookName
    