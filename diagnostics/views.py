from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Endpoint para verificar o status do servidor
def index(request):
    return JsonResponse({"message": "Quantum Diagnostics API is running!"})


@api_view(['GET'])
def obd_diagnostics(request):
    # Simulação de um diagnóstico OBD-II básico
    diagnostic_data = {
        "engine_status": "Running",
        "error_codes": ["P0300", "P0171"],  # Exemplo de códigos de erro
        "battery_health": "Good",
        "oil_level": "Low",
    }
    return Response(diagnostic_data)