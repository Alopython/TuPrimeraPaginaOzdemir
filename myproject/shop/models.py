from django.db import models

# Create your models here.



class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) ->str:
        return self.nombre
    
class compra_equipos(models.Model):
    descripcion = models.TextField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha_fabricacion = models.DateField(null=True)
    origen_fabriacion = models.CharField(max_length=100)
    proyecto = models.ForeignKey(Proyecto,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self) ->str:
         return f"{self.tipo} {self.fecha_fabricacion}"    
     
class venta_equipos(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) ->str:
        return self.nombre
    
    
    
    