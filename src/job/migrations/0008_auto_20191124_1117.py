# Generated by Django 2.2.2 on 2019-11-24 11:17

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20191121_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaljob',
            name='cityname',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), blank=True, max_length=606, null=True, size=6),
        ),
        migrations.AlterField(
            model_name='historicaljob',
            name='expiration_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='historicaljob',
            name='state',
            field=models.CharField(blank=True, choices=[('Nueva', 'Nueva'), ('', 'Sin cambios'), ('Actualizada', 'Actualizada'), ('Inscripción cerrada', 'Inscripción cerrada')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='cityname',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), blank=True, max_length=606, null=True, size=6),
        ),
        migrations.AlterField(
            model_name='job',
            name='expiration_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='state',
            field=models.CharField(blank=True, choices=[('Nueva', 'Nueva'), ('', 'Sin cambios'), ('Actualizada', 'Actualizada'), ('Inscripción cerrada', 'Inscripción cerrada')], max_length=20, null=True),
        ),
    ]
