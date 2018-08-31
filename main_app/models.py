from django.db import models


class Person(models.Model):

    name = models.CharField(verbose_name='name', blank=True, max_length=128)
    surname = models.CharField(verbose_name='surname', blank=True, max_length=128)
    about_desc = models.TextField(verbose_name='about_desc', blank=True)
    birthday = models.DateField(verbose_name='birthday', blank=True)
    location = models.CharField(verbose_name='location', blank=True, max_length=128)
    email = models.CharField(verbose_name='email', blank=True, max_length=254)
    phone = models.CharField(verbose_name='phone', blank=True, max_length=32)

    def __str__(self):
        return '{} {}.'.format(self.name, self.surname)


class Work(models.Model):
    organization = models.CharField(verbose_name='organization', max_length=256)
    region = models.CharField(verbose_name='region', max_length=128)
    site = models.URLField(verbose_name='site')
    position = models.CharField(verbose_name='position', max_length=256)
    official_duties = models.TextField(verbose_name='official_duties')
    start_time = models.DateField(verbose_name='start_time', blank=True)
    end_time = models.DateField(verbose_name="end_time", blank=True, null=True)


class Education(models.Model):
    name = models.CharField(verbose_name="name", max_length=256, blank=True, null=True)
    speciality = models.CharField(verbose_name="speciality", max_length=128, blank=True, null=True)
    description = models.TextField(verbose_name="description", blank=True, null=True)
    end_date = models.DateField(verbose_name="end_date", blank=True, null=True)
    site = models.URLField(verbose_name='site', blank=True, null=True)
    location = models.CharField(verbose_name='location', max_length=256, blank=True, null=True)


