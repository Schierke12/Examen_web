from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
import requests

def perfil(request):
    context = {}
    suscrito(request, context) 
    return render(request, 'core/perfil.html', context)


def logout(request):
    return logout_then_login(request, login_url="login")

def login(request):
    return render(request,  'core/login.html')

def registro(request):
    return render(request,  'core/registro.html')

def carro(request):
    context = {"carro": request.session.get("carro", [])}
    suscrito(request, context)  
    return render(request, 'core/carro.html', context)


def home(request):
    productos = Producto.objects.all()
    productos_con_oferta = Producto.objects.random_con_oferta(4)

    context = {
        'productos': productos,
        'productos_con_oferta': productos_con_oferta, "carro":request.session.get("carro", [])
    }
    suscrito(request, context)
    print(context)
    return render(request, 'core/tienda.html', context)

def suscribir(request):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request, context)
        return render(request, 'core/perfil.html', context)
    else:
        suscrito(request, context)
        return render(request, 'core/perfil.html', context)


def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]

class ProductosPorCategoriaListView(ListView):
    model = Producto
    template_name = 'home'
    context_object_name = 'productos'

    def get_queryset(self):
        categoria = self.kwargs['categoria']
        return Producto.objects.filter(categoria=categoria)


def carroCompras(request, codigo):
    cantidad = request.GET["contador"]
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])

    context = {}
    suscrito(request, context)
    usuario_suscrito = context.get("suscrito", False)

    for i in carro:
        if i[0] == codigo:
            i[4] = int(i[4]) + int(cantidad)
            if producto.oferta:
                precio = producto.nuevoPrecio
            else:
                precio = producto.precio

            total_producto = i[4] * precio

            if request.user.is_authenticated and usuario_suscrito:
                total_producto = total_producto * 0.95 

            total_producto = round(total_producto, 2)

            i[3] = precio
            i[5] = total_producto
            break
    else:
        precio = producto.nuevoPrecio if producto.oferta else producto.precio

        total_producto = precio * int(cantidad)

        if request.user.is_authenticated and usuario_suscrito:
            total_producto = round(total_producto * 0.95)  

        total_producto = round(total_producto, 2)
        total_producto = round(int(total_producto))

        carro.append([codigo, producto.imagen, producto.nombre, precio, cantidad, total_producto])

    request.session['carro'] = carro
    return redirect(to="carro")



def limpiarCarro(request,codigo):
    carro = request.session.get("carro",[])
    for i in carro:
        if i[0] == codigo:
            if int(i[4]) >1:
                i[4] =  int(i[4]) - 1
                i[5] = round((i[3] * int(i[4])) * 0.95)
                break
            else:
                carro.remove(i)
    request.session["carro"] = carro
    return redirect(to="carro")


def realizarCompra(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro",[])
    total = 0
    for i in carro:
        total += i[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for i in carro:
        detalle = Detalle()
        producto = Producto.objects.get(codigo=i[0])
        detalle.imagen = i[1]
        detalle.producto = producto
        detalle.nombre = i[2]
        detalle.precio = i[3]
        detalle.cantidad = i[4]
        detalle.venta = venta
        detalle.total = i[5]
        detalle.save()
        producto.stock = producto.stock - int(i[4])
        producto.save()
        request.session["carro"] = []
    return redirect(to="carro")

def historial(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect(to="login")
    compras = Venta.objects.filter(cliente=request.user)
    detalles = Detalle.objects.filter(venta__in=compras)
    suscrito(request, context)  
    context["compras"] = compras
    context["detalles"] = detalles
    return render(request, 'core/perfil.html', context)


def limpiar(request):
    request.session.flush()
    return redirect(to="home")

# def registro(request):
#     if request.method == "POST":
#         form = Registro(request.POST)
#         if form.is_valid():
#             form.save()
#     else:        
#         form = Registro()
#     return render(request, 'core/registro.html', {'form':form} )


def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la URL deseada
    else:        
        form = Registro()
    return render(request, 'core/registro.html', {'form': form})


def descripcion(request, codigo):
    context = {}
    producto = get_object_or_404(Producto, codigo=codigo)
    productos_relacionados = Producto.objects.filter(categoria=producto.categoria).exclude(codigo=codigo)[:4]
    suscrito(request, context)  
    context['producto'] = producto
    context['productos_relacionados'] = productos_relacionados
    return render(request, 'core/descripcion.html', context)


