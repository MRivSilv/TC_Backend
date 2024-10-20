from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña_hash = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Tareas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=50)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_hora_inicio = models.DateTimeField(null=True, blank=True)
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class ProgresoTareas(models.Model):
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE)
    porcentaje_completado = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


class Notificaciones(models.Model):
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE)
    tipo_notificacion = models.CharField(max_length=100)
    fecha_hora_notificacion = models.DateTimeField()
    estado_notificacion = models.CharField(max_length=50)


class HistoricoTareas(models.Model):
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE)
    estado_anterior = models.CharField(max_length=50)
    estado_nuevo = models.CharField(max_length=50)
    fecha_cambio = models.DateTimeField(auto_now_add=True)


class EncuestaSemanal(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel_estres = models.IntegerField()
    satisfaccion_uso = models.IntegerField()
    fecha_encuesta = models.DateTimeField(auto_now_add=True)
