from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Televisor(models.Model):
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=10)
    pulgadas = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.marca

class Usuario(models.Model):
    nombre = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    usuarios_televisores = models.ManyToManyField(Televisor, through='Votacion', related_name='usuarios_votantes')
    def __str__(self):
        return self.nombre
    

class Votacion(models.Model):
    PUNTUACIONES = [
        (1, 'Muy malo'),
        (2, 'Malo'),
        (3, 'Regular'),
        (4, 'Bueno'),
        (5, 'Muy bueno'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    televisor = models.ForeignKey(Televisor, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=PUNTUACIONES, default=5)
    comentarios = models.TextField(blank=False, null=False)
    fecha_voto=models.DateField(default=timezone.now)
    
 
class CuentaBancaria(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=20)
    banco = models.CharField(max_length=10, choices=[('Caixa', 'Caixa'), ('BBVA', 'BBVA'), ('UNICAJA', 'UNICAJA'), ('ING', 'ING')])
    
    def __str__(self):
        return self.usuario.nombre
    