from rest_framework.serializers import ModelSerializer
from profissional.models import Profissional


class ProfissionalSerializer(ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['id', 'nome', 'crm']