from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from estoque.api import serializers
from estoque import models

class FuncionariosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.FuncionarioSerializer
    queryset = models.Funcionarios.objects.all()

class TamanhoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.TamanhoSerializer
    queryset = models.Tamanho.objects.all()

class FornecedorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.FornecedorSerializer
    queryset = models.Fornecedor.objects.all()

class FornecedorContatoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.FornecedorContatoSerializer
    queryset = models.FornecedorContato.objects.all()

class SolicitacaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.Solicitacao
    queryset = models.Solicitacao.objects.all()