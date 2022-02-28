from django.db import models
from uuid import uuid4
# Create your models here.

class Funcionarios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    matricula = models.CharField(max_length=7)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=18)
    base = models.CharField(max_length=30)
    data_admissao = models.CharField(max_length=20)
    data_demissao = models.CharField(max_length=20)

class Tamanho(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    matricula = models.CharField(max_length=7)
    nome = models.CharField(max_length=100) 
    bota = models.CharField(max_length=4)
    calca = models.CharField(max_length=4)
    camisa = models.CharField(max_length=4)
    jaqueta = models.CharField(max_length=4)

class Fornecedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    fornecedor = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200)

class FornecedorContato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cnpj = models.CharField(max_length=30)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

class Solicitacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    usuario = models.CharField(max_length=70)
    matricula = models.CharField(max_length=7)
    epis = models.CharField(max_length=70)
    cod = models.CharField(max_length=3)
    tipo = models.CharField(max_length=70)
    quantidade = models.CharField(max_length=20)
    tamanho = models.CharField(max_length=20)
    dia = models.CharField(max_length=12)