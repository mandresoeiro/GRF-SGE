from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Usuário customizado com campo de papel e ativo.
    Usa email como campo de login principal.
    """

    email = models.EmailField(unique=True)
    papel = models.CharField(max_length=50, default="aluno")
    ativo = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.email or self.username

    def has_dashboard_access(self) -> bool:
        """
        Permissão customizada: só usuários ativos e staff podem acessar
        o dashboard.
        """
        return self.is_active and self.is_staff

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Group(models.Model):
    """
    Modelo de Grupo para categorizar usuários.
    """

    nome = models.CharField(max_length=100, unique=True)
    enterprise = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        related_name="groups",
        blank=True,
        null=True,
    )
    descricao = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"


class Group_Permissions(models.Model):
    """
    Modelo para associar permissões a grupos.
    """

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="permissions"
    )
    permission_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.group.nome} - {self.permission_name}"

    class Meta:
        verbose_name = "Permissão de Grupo"
        verbose_name_plural = "Permissões de Grupos"


class User_Groups(models.Model):
    """
    Modelo para associar usuários a grupos.
    """

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_groups"
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="user_groups"
    )

    def __str__(self) -> str:
        return f"{self.user.email} - {self.group.nome}"

    class Meta:
        verbose_name = "Grupo de Usuário"
        verbose_name_plural = "Grupos de Usuários"
