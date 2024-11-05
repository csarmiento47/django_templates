from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=30,verbose_name='Nombre')
    address = models.CharField(max_length=30,verbose_name='Dirección')
    price = models.IntegerField(verbose_name='Precio',default=0)
    category = models.CharField(max_length=30,verbose_name='Categoría')
    created_at = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)
    
    class Meta():
        verbose_name = 'artículo'
        verbose_name_plural = 'artículos'
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def clean(self):
        if not self.name:
            raise ValidationError('Debes ingresar un nombre válido')
        if len(self.name) > 30:
            raise ValidationError('El nombre del artículo excede la cantidad máxima permitida [30 caracteres]')
        if self.price < 0:
            raise ValidationError('El precio debe ser un valor mayor o igual a 0')
        
    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)
        
    
class Employee(models.Model):
    rut = models.CharField(primary_key=True,verbose_name='Rut',max_length=15)
    name = models.CharField(max_length=30,verbose_name='Nombre')
    lastname = models.CharField(max_length=30,verbose_name='Apellido')
    dob = models.DateField(verbose_name='Fecha Nacimiento')
    email = models.EmailField(unique=True,verbose_name='Correo electrónico',max_length=100)
    created_at = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)
    
    class Meta():
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        ordering = ['lastname','name','rut']
        
    def __str__(self):
        return f'{self.name} {self.lastname} ({self.rut})'
