# Generated by Django 2.1 on 2018-08-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='education',
            name='site',
            field=models.URLField(blank=True, null=True, verbose_name='site'),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='end_date'),
        ),
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='education',
            name='speciality',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='speciality'),
        ),
    ]