from rest_framework.viewsets import ModelViewSet
from horarios_disponiveis.models import Horario
from .serializers import HorarioSerializer


class HorarioViewSet(ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
