from django.db import models


class Person(models.Model):

    name = models.CharField(verbose_name='name', blank=True, max_length=128)
    surname = models.CharField(verbose_name='surname', blank=True, max_length=128)
    about_desc = models.TextField(verbose_name='about_desc', blank=True)
    birthday = models.DateField(verbose_name='birthday', blank=True)


class Work(models.Model):
    organization = models.CharField(verbose_name='organization', max_length=256)
    region = models.CharField(verbose_name='region', max_length=128)
    site = models.URLField(verbose_name='site')
    position = models.CharField(verbose_name='position', max_length=256)
    official_duties = models.TextField(verbose_name='official_duties')
    start_time = models.DateField(verbose_name='start_time')
