from django.db import models
from django.core.validators import ValidationError
from datetime import date

def validate_min_date(value):
    if value < date(2015, 1, 1):
        raise ValidationError('La fecha debe ser a partir de 2015.')

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=128, blank=False)
    laboratorio = models.OneToOneField(Laboratorio, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, blank=False)
    laboratorio = models.ForeignKey(Laboratorio, on_delete = models.PROTECT)
    f_fabricacion = models.DateField(validators=[validate_min_date])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre

