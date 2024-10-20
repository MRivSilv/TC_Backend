from rest_framework import viewsets
from .models import Usuario, Tareas, ProgresoTareas, Notificaciones, HistoricoTareas, EncuestaSemanal
from .serializers import (
    UsuarioSerializer, TareasSerializer, ProgresoTareasSerializer, 
    NotificacionesSerializer, HistoricoTareasSerializer, EncuestaSemanalSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TareasViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

class ProgresoTareasViewSet(viewsets.ModelViewSet):
    queryset = ProgresoTareas.objects.all()
    serializer_class = ProgresoTareasSerializer

class NotificacionesViewSet(viewsets.ModelViewSet):
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer

class HistoricoTareasViewSet(viewsets.ModelViewSet):
    queryset = HistoricoTareas.objects.all()
    serializer_class = HistoricoTareasSerializer

class EncuestaSemanalViewSet(viewsets.ModelViewSet):
    queryset = EncuestaSemanal.objects.all()
    serializer_class = EncuestaSemanalSerializer
