from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .Serializers import BookSerializers
from rest_framework.response import Response
# Create your views here.
class BookAddAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "book is added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)