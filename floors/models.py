from django.db import models

class Floors(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    status = models.BooleanField(default=True, verbose_name='Activo?')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Piso'
        verbose_name_plural = 'Pisos'
    
    def __str__(self):
        return str(self.name)
    

class ParkingLots(models.Model):
    HORIZONTAL = 'H'
    VERTICAL = 'V'
    ORIENTATION_CHOICES = [
        (HORIZONTAL, 'HORIZONTAL'),
        (VERTICAL, 'VERTICAL'),
    ]
    name = models.CharField(max_length=50, verbose_name='Nombre')
    status = models.BooleanField(default=True, verbose_name='Activo?')
    floor = models.ForeignKey(Floors, editable= True, verbose_name="N° Piso", on_delete=models.PROTECT, blank= False, null=False)
    orientation = models.CharField(
        max_length=1,
        choices=ORIENTATION_CHOICES,
        default=HORIZONTAL,
        verbose_name='Orientación'
    )
    numberrows = models.IntegerField(verbose_name='N° Filas', default= 0)
    numberparq = models.IntegerField(verbose_name='N° Parqueaderos', default= 0)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Estacionamiento'
        verbose_name_plural = 'Estacionamientos'
    
    def __str__(self):
        return str(self.name)