from rest_framework.serializers import ModelSerializer
from horarios_disponiveis.models import Horario


class HorarioSerializer(ModelSerializer):
    class Meta:
        model = Horario
        fields = ['dia_da_semana', 'hora']
