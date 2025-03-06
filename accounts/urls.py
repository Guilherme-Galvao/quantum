from django.urls import path
from .views import register_user, get_user_profile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Gera token de acesso
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Atualiza o token de acesso
    path('register/', register_user, name='register_user'),
    path('profile/', get_user_profile, name='get_user_profile'),
]
