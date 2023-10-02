from django.db import models
from datetime import datetime
# Create your models here.


class Employe(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=15, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now)
