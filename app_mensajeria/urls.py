from django.urls import path
from . import views

urlpatterns = [
    path("enviar_mensaje/", views.enviar_mensaje, name="enviar_mensaje"),
    path("mostar_mensajes/", views.mostrar_mensajes, name="mostrar_mensajes"),
]