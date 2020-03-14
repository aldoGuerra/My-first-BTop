from django.db import models
from django.utils import timezone


class Producto(models.Model):
    usuario_crea = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    clave = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    color = models.CharField(max_length=20)
    talla = models.CharField(max_length=20)
    #precio = models.numericField(10,5)
    #puntos = models.doubleField
    published_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.clave
		
    def __str2__(self):
        return self.nombre

    def __str3__(self):
        return self.descripcion

    def __str4__(self):
        return self.color

    def __str5__(self):
        return self.talla

    #def __price__(self):
    #    return self.precio

    #def __porcnt__(self):
    #    return self.puntos

    def publish(self):
        self.published_date = timezone.now()
        self.save()