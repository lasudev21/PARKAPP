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

class Spaces(models.Model):
    name = models.CharField(default= "", max_length=50, verbose_name='Nombre')
    status = models.BooleanField(default= True, verbose_name='Activo?')
    busy = models.BooleanField(default= False, verbose_name='Ocupado?')
    plate = models.CharField(default= "", blank= True, max_length= 15, verbose_name="Placa")
    income_at = models.DateTimeField(null=True, blank=True,  verbose_name='Fecha ingreso')
    exit_at = models.DateTimeField(null=True, blank=True,  verbose_name='Fecha salida')
    parkinglot = models.ForeignKey(ParkingLots, editable= True, verbose_name="Estacionamiento", on_delete=models.PROTECT, blank= False, null= False)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')
    
    class Meta:
        verbose_name = 'Espacio'
        verbose_name_plural = 'Espacios'
    
    def __str__(self):
        return str(self.name)

class History(models.Model):
    space = models.ForeignKey(Spaces, editable= True, verbose_name="Espacio", on_delete=models.PROTECT, blank= False, null= False)
    plate = models.CharField(default= "", blank= True, max_length= 15, verbose_name="Placa")
    income_at = models.DateTimeField(null=True, blank=True,  verbose_name='Fecha ingreso')
    exit_at = models.DateTimeField(null=True, blank=True,  verbose_name='Fecha salida')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historial'
    
    def __str__(self):
        return str(self.space)
    
    def diferencia_fechas(self):
        # Calcula la diferencia entre las fechas
        diferencia = self.exit_at - self.income_at
        return diferencia