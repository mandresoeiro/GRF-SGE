from django.db import models

# Create your models here.


class Company(models.Model):
    """
    Representa uma empresa cadastrada no sistema.
    """

    name = models.CharField("Nome", max_length=255)
    address = models.TextField("Endereço")
    phone = models.CharField("Telefone", max_length=20)
    email = models.EmailField("E-mail", unique=True)
    owner = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.CASCADE,
        related_name="companies",
        verbose_name="Proprietário",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
