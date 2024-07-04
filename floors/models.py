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
    

class Rows(models.Model):
    HORIZONTAL = 'H'
    VERTICAL = 'V'
    ORIENTATION_CHOICES = [
        (HORIZONTAL, 'Horizontal'),
        (VERTICAL, 'Vertical'),
    ]
    name = models.CharField(max_length=50, verbose_name='Nombre')
    status = models.BooleanField(default=True, verbose_name='Activo?')
    floor = models.ForeignKey(Floors, editable= True, verbose_name="N° Piso", on_delete=models.PROTECT, blank= False, null=False)
    orientation = models.CharField(
        max_length=1,
        choices=ORIENTATION_CHOICES,
        default=HORIZONTAL,
    )
    numberparq = models.IntegerField(verbose_name='N° Parqueaderos')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Fila'
        verbose_name_plural = 'Filas'
    
    def __str__(self):
        return str(self.name)