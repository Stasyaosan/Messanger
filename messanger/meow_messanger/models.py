from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(max_length=100, verbose_name='О себе')
