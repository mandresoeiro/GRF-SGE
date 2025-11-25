from django.contrib.auth.models import AbstractUser
from django.db import models


from typing import Any


class CustomUser(AbstractUser):
    papel: models.CharField = models.CharField(max_length=50, default="aluno")
    ativo: models.BooleanField = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.username

    def has_dashboard_access(self) -> bool:
        """Exemplo de permissão customizada: só usuários ativos e staff podem acessar o dashboard."""
        return self.is_active and self.is_staff
