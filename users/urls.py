from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users import views

app_name = "users"

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register/', views.UsersRegistrationView.as_view(), name='register'),
    path('users/<int:id>/', views.UserView.as_view(), name='users'),
]
