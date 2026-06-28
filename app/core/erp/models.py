from django.db import models
from datetime import datetime

class Type (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Category (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Employee(models.Model):
    category = models.ManyToManyField(Category, verbose_name='Categoria')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Tipo')
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0, verbose_name='Edad')
    salary = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    state = models.BooleanField(default=True, verbose_name='Estado')
    #gender = models.CharField(max_length=50, verbose_name='Sexo')
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True, verbose_name='cvitae')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
