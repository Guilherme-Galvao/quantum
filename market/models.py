from django.db import models


class MarketplaceItem(models.Model):
    name = models.CharField(max_length=100)  # Nome da peça
    description = models.TextField()  # Descrição detalhada da peça
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço da peça
    stock = models.IntegerField()  # Quantidade disponível no estoque
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do item

    def __str__(self):
        return self.name
