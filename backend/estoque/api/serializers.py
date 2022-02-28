from rest_framework import serializers
from estoque import models

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Funcionarios
        fields = '__all__'

class TamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tamanho
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fornecedor
        fields = '__all__'

class FornecedorContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FornecedorContato
        fields = '__all__'

class Solicitacao(serializers.ModelSerializer):
    class Meta:
        model = models.Solicitacao
        fields = '__all__'