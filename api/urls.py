from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, TareasViewSet, ProgresoTareasViewSet,
    NotificacionesViewSet, HistoricoTareasViewSet, EncuestaSemanalViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'tareas', TareasViewSet)
router.register(r'progreso_tareas', ProgresoTareasViewSet)
router.register(r'notificaciones', NotificacionesViewSet)
router.register(r'historico_tareas', HistoricoTareasViewSet)
router.register(r'encuesta_semanal', EncuestaSemanalViewSet)

urlpatterns = router.urls
