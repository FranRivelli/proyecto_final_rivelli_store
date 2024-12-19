from django.urls import path
from app_tienda import views

urlpatterns = [
    #Páginas
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    path("product/", views.product, name="product"),
    path("contact/", views.contact, name="contact"),
    path("contact/contacto", views.contacto, name="contacto"),
    #Zapatillas
    path('zapatillas/', views.zapatillas, name="zapatillas"),
    path('zapatillas/formulario/', views.formulario_zapatillas, name="formulario_zapatillas"),
    path('zapatillas/exito/', views.registro_zapatillas, name="registro_zapatillas"),
    path('zapatillas/eliminar/<int:id>', views.eliminar_zapatilla, name="eliminar_zapatilla"),
    path('zapatillas/editar/<int:id>', views.editar_zapatilla, name="editar_zapatilla"),
    path('zapatillas/detalle/<int:pk>', views.ZapatillaDetailView.as_view(), name="detalle_zapatilla"),
    #Botines
    path('botines/', views.botines, name="botines"),
    path('botines/formulario/', views.formulario_botines, name="formulario_botines"),
    path('botines/exito/', views.registro_botines, name="registro_botines"),
    path('botines/eliminar/<int:id>', views.eliminar_botin, name="eliminar_botin"),
    path('botines/editar/<int:id>', views.editar_botin, name="editar_botin"),
    path('botines/detalle/<int:pk>', views.BotinDetailView.as_view(), name="detalle_botin"),
    #Ropa
    path('ropa/', views.ropa, name="ropa"),
    path('ropa/formulario/', views.formulario_ropa, name="formulario_ropa"),
    path('ropa/exito/', views.registro_ropa, name="registro_ropa"),
    path('ropa/eliminar/<int:id>', views.eliminar_ropa, name="eliminar_ropa"),
    path('ropa/editar/<int:id>', views.editar_ropa, name="editar_ropa"),
    path('ropa/detalle/<int:pk>', views.RopaDetailView.as_view(), name="detalle_ropa"),
    #Otros productos
    path('otros/', views.otros, name="otros"),
    path('otros/formulario/', views.formulario_otros, name="formulario_otros"),
    path('otros/exito/', views.registro_otros, name="registro_otros"),
    path('otros/eliminar/<int:id>', views.eliminar_otros, name="eliminar_otros"),
    path('otros/editar/<int:id>', views.editar_otros, name="editar_otros"),
    path('otros/detalle/<int:pk>', views.OtrosDetailView.as_view(), name="detalle_otros"),
    #Vendedores
    path('vendedores/', views.vendedores, name="vendedores"),
    path('vendedores/formulario/', views.formulario_vendedores, name="formulario_vendedores"),
    path('vendedores/exito/', views.registro_vendedores, name="registro_vendedores"),
    path('vendedores/eliminar/<int:id>', views.eliminar_vendedor, name="eliminar_vendedor"),
    path('vendedores/editar/<int:id>', views.editar_vendedor, name="editar_vendedor"),
    path('vendedores/detalle/<int:pk>', views.VendedoresDetailView.as_view(), name="detalle_vendedores"),
    #Clientes
    path('clientes/', views.clientes, name="clientes"),
    path('clientes/formulario/', views.formulario_clientes, name="formulario_clientes"),
    path('clientes/exito/', views.registro_clientes, name="registro_clientes"),
    path('clientes/eliminar/<int:id>', views.eliminar_cliente, name="eliminar_cliente"),
    path('clientes/editar/<int:id>', views.editar_cliente, name="editar_cliente"),
    path('clientes/detalle/<int:pk>', views.ClientesDetailView.as_view(), name="detalle_clientes"),
    #Inicio sesión, registro, cerrar sesión
    path("inicio_sesion/", views.inicio_sesion, name="inicio_sesion"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("registro_usuario/", views.registro_usuario, name="registro_usuario"),
    #Mostrar y editar perfil, cambiar contraseña
    path("mostrar_perfil", views.mostrar_perfil, name="mostrar_perfil"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),
    path("cambiar_contraseña", views.cambiar_contraseña, name="cambiar_contraseña"),
]

