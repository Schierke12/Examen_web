from django.db import models
import random
from datetime import datetime
from django.contrib.auth.models import User

#genera un numero aleatorio entre 5 y 15
def generar_oferta():
    return random.randint(5, 15)

class ProductoManager(models.Manager):
    def random_con_oferta(self, count):
        # Obtiene 'count' productos aleatorios
        productos = self.get_queryset().filter(oferta=True).order_by('?')[:count]
        # Genera una oferta aleatoria para cada producto
        for producto in productos:
            if producto.descuento:  # Verifica si la oferta ya ha sido generada anteriormente
                # producto.descuento
                producto.nuevoPrecio = int(producto.precio - (producto.descuento / 100) * producto.precio)
                producto.save()
            else:
                producto.descuento = generar_oferta()
                producto.nuevoPrecio = int(producto.precio - (producto.descuento / 100) * producto.precio)
                producto.save()

        return productos


class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=60, default="")
    precio = models.IntegerField()
    descuento = models.IntegerField(default=0)
    stock = models.IntegerField()
    puntaje = models.DecimalField(max_digits=2, decimal_places=1)
    imagen = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, default="")
    oferta = models.BooleanField(default=False)
    nuevoPrecio = models.IntegerField(default=0)
    objects = ProductoManager()

    #esto sirve para como se vera en admin los productos
    def __str__(self) :
        return self.codigo + ' ' + self.nombre
    
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default=datetime.now)
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()

    def __str__(self) :
        return str(self.id) + ' ' + self.cliente.username+" "+str(self.fecha)[0:16] 

STATUS_CHOICES = (
    ('en preparacion', 'EN PREPARACION'),
    ('saliendo de la sucursal', 'SALIENDO DE LA SUCURSAL'),
    ('en camino', 'EN CAMINO'),
    ('entregado', 'ENTREGADO'),
)

class Detalle(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    imagen = models.CharField(max_length=200, default="")
    nombre = models.CharField(max_length=60, default="")
    estado = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES, 
        default='en preparacion'
    )
    fecha = models.DateField(default=datetime.now())
    total = models.IntegerField(default=0)

    def __str__(self) :
        return str(self.id) + ' ' + self.producto.nombre+" "+str(self.venta.id) 





    
