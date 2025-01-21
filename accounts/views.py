from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer

@api_view(['POST'])
def register_user(request):
    data = request.data
    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    UserProfile.objects.create(user=user)  # Cria o perfil automaticamente
    return Response({"message": "Usuário registrado com sucesso!"})

@api_view(['GET'])
def get_user_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)
