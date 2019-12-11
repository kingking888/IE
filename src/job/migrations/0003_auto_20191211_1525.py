# Generated by Django 2.2.2 on 2019-12-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20191210_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalcompany',
            name='company_name',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]
