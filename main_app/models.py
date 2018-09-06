from django.db import models


class Organization(models.Model):
    id = models.IntegerField(verbose_name='id', unique=True, primary_key=True)
    site = models.URLField(verbose_name='site')
    name = models.CharField(verbose_name='name', max_length=256)
    address = models.TextField(verbose_name='address')
    local_url = models.URLField(verbose_name='local_url')
    phone = models.CharField(verbose_name='phone', max_length=32)
    desc = models.TextField(verbose_name='description')
    slug = models.SlugField(verbose_name='slug', blank=True, null=True)
    yandex_map = models.TextField(verbose_name='yandex_map', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


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
    organization = models.ForeignKey(Organization, verbose_name='organization', on_delete=models.CASCADE)
    region = models.CharField(verbose_name='region', max_length=128)
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


