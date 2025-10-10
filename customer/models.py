from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerModel(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    nome_rua = models.CharField(max_length=100, blank=True, null=True)
    numero_residencia = models.CharField(max_length=100, blank=True, null=True)
    nome_bairro = models.CharField(max_length=100, blank=True, null=True)
    nome_cidade = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length= 100, blank=False)
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return f"{self.username} - {self.cpf}"