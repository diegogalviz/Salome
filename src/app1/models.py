from django.db import models
from datetime import datetime


# Create your models here.
class Type_employee(models.Model):
    name = models.CharField(max_length=150, verbose_name='nombre_tipo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']
        app_label = 'app1'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre_categoria')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'categoria'
        app_label = 'app1'


class Employee(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    CC = models.CharField(max_length=10, unique=True, verbose_name='CC')
    date_join = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    data_created = models.DateTimeField(auto_now=True)
    data_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    # gender = models.CharField(max_length=50)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.ImageField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type_employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        db_table = 'empleados'
        ordering = ['id']
        app_label = 'app1'
