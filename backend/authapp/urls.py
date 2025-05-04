from django.urls import path
from .views import StudentRegisterAPIView,StudentLoginAPIView

urlpatterns = [
    path('register/', StudentRegisterAPIView.as_view(), name='student-list-create'),
    path('login/', StudentLoginAPIView.as_view(), name='student-login')
    
]
