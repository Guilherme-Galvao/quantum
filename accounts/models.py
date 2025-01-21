from django.db import models
from django.contrib.auth.models import User

# Modelo de perfil do usuário
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")  # Relaciona com o User
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Número de telefone
    address = models.TextField(blank=True, null=True)  # Endereço
    preferred_language = models.CharField(max_length=50, default="Português")  # Idioma preferido
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)  # Foto do perfil
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do perfil

    def __str__(self):
        return f"{self.user.username}'s Profile"
