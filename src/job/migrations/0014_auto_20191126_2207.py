# Generated by Django 2.2.2 on 2019-11-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_auto_20191126_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
