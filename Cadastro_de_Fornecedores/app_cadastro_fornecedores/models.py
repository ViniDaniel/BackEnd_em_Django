from django.db import models

# Create your models here.

class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    cnpj = models.IntegerField()
    endereco = models.TextField(max_length=500)
    celular = models.IntegerField
    email = models.TextField(max_length=255)
    produto = models.TextField(max_length=255)
    