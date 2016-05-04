from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField()
    contrasena = models.CharField(max_length=255)
    telefono = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='images/usuario', default='images/no-img.png')
    administrador = models.BooleanField(default=False)
    video = models.FileField(upload_to='videos', default='images/no-img.png')

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellidos)

class Direccion(models.Model):
    ciudad = models.CharField(max_length=25)
    municipio = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)
    codigo_postal = models.CharField(max_length=6)
    direccion = models.TextField()
    colonia = models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario)

    def __str__(self):
        return "{0}, {1}".format(self.ciudad, self.estado)

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    foto = models.ImageField(upload_to='images/producto')
    ultima_modificacion = models.CharField(max_length=60)
    aprobado = models.BooleanField(default=False)
    vendido = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario)
    categoria = models.ForeignKey(Categoria)

    def __str__(self):
        return self.nombre

class Flete(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    producto = models.ForeignKey(Producto)
    cliente = models.ForeignKey(Usuario)
    entregado = models.BooleanField(default=False)
    precio_total = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=40)
    coordenadasX = models.DecimalField(max_digits=12, decimal_places=2)
    coordenadasY = models.DecimalField(max_digits=12, decimal_places=2)
    flete = models.ForeignKey(Flete)