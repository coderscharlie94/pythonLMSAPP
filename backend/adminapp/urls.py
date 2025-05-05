from django.urls import path
from .views import BookAddAPIView

urlpatterns = [
    path('add/', BookAddAPIView.as_view(), name='Add-Book')
    
]
