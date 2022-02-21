from rest_framework.serializers import ModelSerializer
from cliente.models import Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'telefone']
