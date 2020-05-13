from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(verbose_name="Nombre")
    last_name=models.CharField(verbose_name="Apellidos")
    identification=models.CharField(verbose_name="Identificación")
    email=models.EmailField(verbose_name="Correo electrónico")
    created=models.DateTimeField(auto_now_add=True)
    addres=models.CharField(verbose_name="Dirección")
