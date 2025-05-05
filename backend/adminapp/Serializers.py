from rest_framework import serializers
from .models import Book
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=["id","bookName","bookAuthor","bookPrice"]
        
    def AddBook(self,validated_data):
        books=Book(
            bookName=validated_data['bookName'],
            bookAuthor=validated_data['bookAuthor'],
            bookPrice=validated_data['bookPrice']
        )
        books.save()
        return books