from django.urls import path
from .views import RegisterView, UserProfileListCreateView, UserProfileDetailView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', LoginView.as_view(), name='token_obtain_pair'),  # JWT login
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('profiles/', UserProfileListCreateView.as_view(), name='profile_list_create'),
   path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),
]