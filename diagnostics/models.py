from django.db import models
from django.contrib.auth.models import User

# Modelo para históricos de diagnósticos
class DiagnosticHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o usuário
    vehicle = models.CharField(max_length=100)  # Nome ou modelo do veículo
    diagnostic_date = models.DateTimeField(auto_now_add=True)  # Data do diagnóstico
    engine_status = models.CharField(max_length=100)  # Status do motor
    error_codes = models.JSONField()  # Armazena os códigos de erro (formato JSON)
    notes = models.TextField(blank=True, null=True)  # Notas adicionais sobre o diagnóstico

    def __str__(self):
        return f"{self.vehicle} - {self.diagnostic_date}"
