from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, UserProfileForm


# Create your views here.
@login_required
def cambiar_contraseña(request):
    usuario = request.user
    if request.method == "POST":
        form_password = PasswordChangeForm(usuario, request.POST)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, usuario)
            return redirect('mostrar_perfil')
    else:
        form_password = PasswordChangeForm(usuario)
    return render(request, "app_tienda/forms/cambiar_contraseña.html", {"form_password":form_password})

@login_required
def mostrar_perfil(request):
    return render(request, "app_tienda/mostrar_perfil.html")

@login_required
def editar_perfil(request):
    usuario = request.user
    profile, _ = Perfil.objects.get_or_create(user=usuario)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=usuario)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("mostrar_perfil")
        else:
            return redirect('mostrar_perfil')
    else:
        user_form = UserUpdateForm(instance=usuario)
        profile_form = UserProfileForm(instance=profile)
    return render(request, "app_tienda/forms/editar_perfil.html", {"user_form":user_form, "profile_form":profile_form})

def inicio_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "¡Inicio de sesión exitoso!")
            return render(request, "app_tienda/index.html")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "app_tienda/forms/inicio_sesion.html")

def cerrar_sesion(request):
    logout(request)
    messages.success(request, f"Sesión finalizada con éxito. Hasta la próxima!")
    return redirect('inicio')

def registro_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Registro exitoso!")
            return redirect('registro_usuario')
    else:
        form = UserCreationForm
    return render(request, "app_tienda/forms/registro_usuario.html", {"form":form})

def inicio(request):
    return render(request, "app_tienda/index.html")

def about(request):
    return render(request, "app_tienda/about.html")

def product(request):
    return render(request, "app_tienda/product.html")

def contact(request):
    return render(request, "app_tienda/contact.html")

def zapatillas(request):
    query = request.GET.get('q')
    if query:
        zapatillas = Zapatillas.objects.filter(modelo__icontains=query)
    else:
        zapatillas = Zapatillas.objects.all()
    return render(request, "app_tienda/zapatilla.html", {"zapatillas":zapatillas, "query":query})

def botines(request):
    query = request.GET.get('q')
    if query:
        botines = Botines.objects.filter(modelo__icontains=query)
    else:
        botines = Botines.objects.all()
    return render(request, "app_tienda/botines.html", {"botines":botines, "query":query})

def ropa(request):
    query = request.GET.get('q')
    if query:
        ropa = Ropa.objects.filter(modelo__icontains=query)
    else:
        ropa = Ropa.objects.all()
    return render(request, "app_tienda/ropa.html", {"ropa":ropa, "query":query})

def otros(request):
    query = request.GET.get('q')
    if query:
        otros = Otros_Productos.objects.filter(producto__icontains=query)
    else:
        otros = Otros_Productos.objects.all()
    return render(request, "app_tienda/otros.html", {"otros":otros, "query":query})

@login_required
def vendedores(request):
    query = request.GET.get('q')
    if query:
        vendedores = Vendedores.objects.filter(apellido__icontains=query)
    else:
        vendedores = Vendedores.objects.all()
    return render(request, "app_tienda/vendedores.html", {"vendedores":vendedores, "query":query})

@login_required
def clientes(request):
    query = request.GET.get('q')
    if query:
        clientes = Clientes.objects.filter(apellido__icontains=query)
    else:
        clientes = Clientes.objects.all()
    return render(request, "app_tienda/clientes.html", {"clientes":clientes, "query":query})

@login_required
def formulario_zapatillas(request):
    if request.method == "POST":
        modelo = request.POST.get("modelo")
        precio = request.POST.get("precio")
        talle_arg = request.POST.get("talle_arg")
        vendedor = request.POST.get("vendedor")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        zapatillas = Zapatillas(
            modelo=modelo,
            precio=precio,
            talle_arg=talle_arg,
            vendedor=vendedor,
            descripcion=descripcion,
            imagen=imagen,
        )
        zapatillas.save()
        return redirect('registro_zapatillas')
    return render(request, "app_tienda/forms/zapatillas_formularios.html")

@login_required
def registro_zapatillas(request):
    return render(request, "app_tienda/forms/registro_zapatillas.html")

@login_required
def formulario_botines(request):
    if request.method == "POST":
        modelo = request.POST.get("modelo")
        precio = request.POST.get("precio")
        talle_arg = request.POST.get("talle_arg")
        vendedor = request.POST.get("vendedor")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        botines = Botines(
            modelo=modelo,
            precio=precio,
            talle_arg=talle_arg,
            vendedor=vendedor,
            descripcion=descripcion,
            imagen=imagen,
        )
        botines.save()
        return redirect('registro_botines')
    return render(request, "app_tienda/forms/botines_formularios.html")

@login_required
def registro_botines(request):
    return render(request, "app_tienda/forms/registro_botines.html")

@login_required
def formulario_ropa(request):
    if request.method == "POST":
        modelo = request.POST.get("modelo")
        precio = request.POST.get("precio")
        talle_arg = request.POST.get("talle_arg")
        vendedor = request.POST.get("vendedor")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        ropa = Ropa(
            modelo=modelo,
            precio=precio,
            talle_arg=talle_arg,
            vendedor=vendedor,
            descripcion=descripcion,
            imagen=imagen,
        )
        ropa.save()
        return redirect('registro_ropa')
    return render(request, "app_tienda/forms/ropa_formularios.html")

@login_required
def registro_ropa(request):
    return render(request, "app_tienda/forms/registro_ropa.html")

@login_required
def formulario_otros(request):
    if request.method == "POST":
        producto = request.POST.get("modelo")
        precio = request.POST.get("precio")
        vendedor = request.POST.get("vendedor")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        otros = Otros_Productos(
            producto=producto,
            precio=precio,
            vendedor=vendedor,
            descripcion=descripcion,
            imagen=imagen,
        )
        otros.save()
        return redirect('registro_otros')
    return render(request, "app_tienda/forms/otros_formularios.html")

@login_required
def registro_otros(request):
    return render(request, "app_tienda/forms/registro_otros.html")

@login_required
def formulario_vendedores(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        vendedores = Vendedores(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )
        vendedores.save()
        return redirect('registro_vendedores')
    return render(request, "app_tienda/forms/vendedores_formularios.html")

@login_required
def registro_vendedores(request):
    return render(request, "app_tienda/forms/registro_vendedores.html")

@login_required
def formulario_clientes(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        clientes = Clientes(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )
        clientes.save()
        return redirect('registro_clientes')
    return render(request, "app_tienda/forms/clientes_formularios.html")

@login_required
def registro_clientes(request):
    return render(request, "app_tienda/forms/registro_clientes.html")

@login_required
def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        descripcion = request.POST.get("descripcion")
        contacto = Contacto(
            nombre=nombre,
            email=email,
            telefono=telefono,
            descripcion=descripcion
        )
        contacto.save()
        return redirect('contact')
    return render(request, "app_tienda/contact.html")

@login_required
def eliminar_zapatilla(request, id):
    zapatilla = Zapatillas.objects.get(id=id)
    zapatilla.delete()
    return redirect("zapatillas")

@login_required
def editar_zapatilla(request, id):
    zapatilla = get_object_or_404(Zapatillas, id=id)
    if request.method == "POST":
        zapatilla.modelo = request.POST['modelo']
        zapatilla.precio = request.POST['precio']
        zapatilla.talle_arg = request.POST['talle_arg']
        zapatilla.vendedor = request.POST['vendedor']
        zapatilla.descripcion = request.POST['descripcion']
        if 'imagen' in request.FILES:  
            zapatilla.imagen = request.FILES['imagen']
        zapatilla.save()
        return redirect('zapatillas')
    return render(request, "app_tienda/forms/editar_zapatilla.html", {"zapatilla": zapatilla})

@login_required
def eliminar_botin(request, id):
    botin = Botines.objects.get(id=id)
    botin.delete()
    return redirect("botines")

@login_required
def editar_botin(request, id):
    botin = get_object_or_404(Botines, id=id)
    if request.method == "POST":
        botin.modelo = request.POST['modelo']
        botin.precio = request.POST['precio']
        botin.talle_arg = request.POST['talle_arg']
        botin.vendedor = request.POST['vendedor']
        botin.descripcion = request.POST['descripcion']
        if 'imagen' in request.FILES:  
            botin.imagen = request.FILES['imagen']
        botin.save()
        return redirect('botines')
    return render(request, "app_tienda/forms/editar_botin.html", {"botin": botin})

@login_required
def eliminar_ropa(request, id):
    ropa = Ropa.objects.get(id=id)
    ropa.delete()
    return redirect("ropa")

@login_required
def editar_ropa(request, id):
    ropa = get_object_or_404(Ropa, id=id)
    if request.method == "POST":
        ropa.modelo = request.POST['modelo']
        ropa.precio = request.POST['precio']
        ropa.talle_arg = request.POST['talle_arg']
        ropa.vendedor = request.POST['vendedor']
        ropa.descripcion = request.POST['descripcion']
        if 'imagen' in request.FILES:  
            ropa.imagen = request.FILES['imagen']
        ropa.save()
        return redirect('ropa')
    return render(request, "app_tienda/forms/editar_ropa.html", {"ropa": ropa})

@login_required
def eliminar_otros(request, id):
    otros = Otros_Productos.objects.get(id=id)
    otros.delete()
    return redirect("otros")

@login_required
def editar_otros(request, id):
    otros = get_object_or_404(Otros_Productos, id=id)
    if request.method == "POST":
        otros.producto = request.POST['producto']
        otros.precio = request.POST['precio']
        otros.vendedor = request.POST['vendedor']
        otros.descripcion = request.POST['descripcion']
        if 'imagen' in request.FILES:  
            otros.imagen = request.FILES['imagen']
        otros.save()
        return redirect('otros')
    return render(request, "app_tienda/forms/editar_otros.html", {"otros": otros})

@login_required
def eliminar_vendedor(request, id):
    vendedor = Vendedores.objects.get(id=id)
    vendedor.delete()
    return redirect("vendedores")

@login_required
def editar_vendedor(request, id):
    vendedor = get_object_or_404(Vendedores, id=id)
    if request.method == "POST":
        vendedor.nombre = request.POST['nombre']
        vendedor.apellido = request.POST['apellido']
        vendedor.email = request.POST['email']
        vendedor.telefono = request.POST['telefono']
        vendedor.save()
        return redirect('vendedores')
    return render(request, "app_tienda/forms/editar_vendedor.html", {"vendedor": vendedor})

@login_required
def eliminar_cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect("clientes")

@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == "POST":
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.email = request.POST['email']
        cliente.telefono = request.POST['telefono']
        cliente.save()
        return redirect('clientes')
    return render(request, "app_tienda/forms/editar_cliente.html", {"cliente": cliente})

class ZapatillaDetailView(DetailView):
    model = Zapatillas
    template_name = "app_tienda/detalles/zapatilla_detalles.html"

class BotinDetailView(DetailView):
    model = Botines
    template_name = "app_tienda/detalles/botin_detalles.html"

class RopaDetailView(DetailView):
    model = Ropa
    template_name = "app_tienda/detalles/ropa_detalles.html"

class OtrosDetailView(DetailView):
    model = Otros_Productos
    template_name = "app_tienda/detalles/otros_detalles.html"

class VendedoresDetailView(DetailView):
    model = Vendedores
    template_name = "app_tienda/detalles/vendedor_detalles.html"

class ClientesDetailView(DetailView):
    model = Clientes
    template_name = "app_tienda/detalles/cliente_detalles.html"