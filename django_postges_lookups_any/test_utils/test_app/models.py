from django.db import models


class ModelA(models.Model):
    name = models.CharField('Test Name A', max_length=100)
    external_id = models.PositiveIntegerField('Test ID A')


class ModelB(models.Model):
    name = models.CharField('Test Name B', max_length=100)
    external_id = models.PositiveIntegerField('Test ID B')
