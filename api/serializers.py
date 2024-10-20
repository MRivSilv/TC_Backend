from rest_framework import serializers
from .models import Usuario, Tareas, ProgresoTareas, Notificaciones, HistoricoTareas, EncuestaSemanal

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'

class ProgresoTareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoTareas
        fields = '__all__'

class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = '__all__'

class HistoricoTareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoTareas
        fields = '__all__'

class EncuestaSemanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncuestaSemanal
        fields = '__all__'
