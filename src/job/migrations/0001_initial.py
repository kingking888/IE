# Generated by Django 2.2.2 on 2020-01-16 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('capital_id', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Community',
                'verbose_name_plural': 'Communities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.URLField(null=True)),
                ('description', models.TextField(null=True)),
                ('resume', models.CharField(blank=True, max_length=300, null=True)),
                ('city_name', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('offers', models.IntegerField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='job.City')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('inglés', 'inglés'), ('francés', 'francés'), ('alemán', 'alemán'), ('italiano', 'italiano'), ('ruso', 'ruso'), ('chino', 'chino'), ('japonés', 'japonés'), ('canadiense', 'canadiense'), ('portugués', 'portugués'), ('euskera', 'euskera'), ('catalán', 'catalán'), ('gallego', 'gallego'), ('vasco', 'vasco'), ('valencianocastellano', 'valencianocastellano'), ('español', 'español'), ('danés', 'danés'), ('sueco', 'sueco'), ('suizo', 'suizo'), ('holandés', 'holandés'), ('noruego', 'noruego'), ('finés', 'finés'), ('lapón', 'lapón'), ('rumano', 'rumano'), ('polaco', 'polaco'), ('eslovaco', 'eslovaco'), ('checo', 'checo'), ('maltés', 'maltés'), ('árabe', 'árabe')], default='', max_length=15)),
                ('level', models.CharField(choices=[('C2', 'C2'), ('C1', 'C1'), ('B2', 'B2'), ('B1', 'B1'), ('A2', 'A2'), ('A1', 'A1')], default='', max_length=2)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ['name', 'level'],
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('community_number', models.IntegerField(blank=True, null=True)),
                ('capital_id', models.IntegerField(null=True)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='job.Community')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='job.Country')),
            ],
            options={
                'verbose_name': 'Province',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField(null=True)),
                ('state', models.CharField(blank=True, choices=[('Nueva', 'Nueva'), ('', 'Sin cambios'), ('Actualizada', 'Actualizada'), ('Inscripción cerrada', 'Inscripción cerrada')], max_length=30, null=True)),
                ('type', models.CharField(choices=[('ofertas-internacionales', 'Empleo internacional'), ('trabajo', 'Empleo nacional'), ('primer-empleo', 'Primer empleo')], default='trabajo', max_length=30)),
                ('summary', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=606, null=True, size=6)),
                ('_experience', models.CharField(blank=True, max_length=40, null=True)),
                ('_salary', models.CharField(blank=True, max_length=40, null=True)),
                ('_contract', models.CharField(blank=True, max_length=40, null=True)),
                ('_working_day', models.CharField(blank=True, max_length=40, null=True)),
                ('minimum_years_of_experience', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('recommendable_years_of_experience', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('minimum_salary', models.PositiveIntegerField(blank=True, null=True)),
                ('maximum_salary', models.PositiveIntegerField(blank=True, null=True)),
                ('working_day', models.CharField(choices=[('Jornada sin especificar', 'sin especificar'), ('Jornada Intensiva', 'intensiva'), ('Jornada Indiferente', 'flexible'), ('Jornada Parcial', 'parcial'), ('Jornada Fin de Semana', 'fin de semana'), ('Jornada Completa', 'completa'), ('Jornada Tele Trabajo', 'tele trabajo')], default='Sin especificar', max_length=30)),
                ('contract', models.CharField(choices=[('Contrato sin especificar', 'sin especificar'), ('Contrato Prácticas', 'prácticas'), ('Contrato Indefinido', 'indefinido'), ('Contrato Autónomo o freelance', 'autónomo o freelance'), ('Contrato Fijo discontinuo', 'fijo discontinuo'), ('Contrato Formativo', 'formativo'), ('Contrato De duración determinada', 'de duración determinada')], default='Contrato sin especificar', max_length=40)),
                ('cityname', django_mysql.models.ListCharField(models.CharField(max_length=100), blank=True, max_length=606, null=True, size=6)),
                ('provincename', models.CharField(blank=True, max_length=100, null=True)),
                ('countryname', models.CharField(max_length=30, null=True)),
                ('nationality', models.CharField(max_length=30)),
                ('first_publication_date', models.DateField(blank=True, default=None, null=True)),
                ('last_update_date', models.DateField(blank=True, default=None, null=True)),
                ('expiration_date', models.DateField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('functions', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('it_is_offered', models.TextField(blank=True, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('area', models.CharField(choices=[('Educación, formación', 'Educación, formación'), ('Tecnología e informática', 'Tecnología e informática'), ('Sanidad, salud y servicios sociales', 'Sanidad, salud y servicios sociales'), ('Medios, editorial y artes gráficas', 'Medios, editorial y artes gráficas'), ('Compras, logística y transporte', 'Compras, logística y transporte'), ('Administrativos y secretariado', 'Administrativos y secretariado'), ('Profesionales, artes y oficios', 'Profesionales, artes y oficios'), ('Telecomunicaciones', 'Telecomunicaciones'), ('Legal', 'Legal'), ('Internet', 'Internet'), ('Banca y seguros', 'Banca y seguros'), ('Calidad, I+D, PRL y medio ambiente', 'Calidad, I+D, PRL y medio ambiente'), ('Recursos humanos', 'Recursos humanos'), ('Comercial, ventas', 'Comercial, ventas'), ('Ingeniería y producción', 'Ingeniería y producción'), ('Atención al cliente', 'Atención al cliente'), ('Construcción e inmobiliaria', 'Construcción e inmobiliaria'), ('Hostelería, Turismo', 'Hostelería, Turismo'), ('Administración de Empresas', 'Administración de Empresas'), ('Marketing y comunicación', 'Marketing y comunicación')], max_length=40)),
                ('category_level', models.CharField(choices=[('Mandos', 'Mandos'), ('Empleados', 'Empleados'), ('Técnicos', 'Técnicos'), ('Dirección', 'Dirección'), ('Sin especificar', 'Sin especificar')], default='Sin especificar', max_length=20, null=True)),
                ('vacancies', models.PositiveIntegerField(blank=True, null=True)),
                ('registered_people', models.PositiveIntegerField(default=0)),
                ('vacancies_update', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('cities', models.ManyToManyField(blank=True, null=True, related_name='jobs', to='job.City')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.Company')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.Country')),
                ('languages', models.ManyToManyField(blank=True, null=True, related_name='jobs', to='job.Language')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.Province')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'ordering': ['-created_at', 'name'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalJob',
            fields=[
                ('id', models.IntegerField(db_index=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField(null=True)),
                ('state', models.CharField(blank=True, choices=[('Nueva', 'Nueva'), ('', 'Sin cambios'), ('Actualizada', 'Actualizada'), ('Inscripción cerrada', 'Inscripción cerrada')], max_length=30, null=True)),
                ('type', models.CharField(choices=[('ofertas-internacionales', 'Empleo internacional'), ('trabajo', 'Empleo nacional'), ('primer-empleo', 'Primer empleo')], default='trabajo', max_length=30)),
                ('summary', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=606, null=True, size=6)),
                ('_experience', models.CharField(blank=True, max_length=40, null=True)),
                ('_salary', models.CharField(blank=True, max_length=40, null=True)),
                ('_contract', models.CharField(blank=True, max_length=40, null=True)),
                ('_working_day', models.CharField(blank=True, max_length=40, null=True)),
                ('minimum_years_of_experience', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('recommendable_years_of_experience', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('minimum_salary', models.PositiveIntegerField(blank=True, null=True)),
                ('maximum_salary', models.PositiveIntegerField(blank=True, null=True)),
                ('working_day', models.CharField(choices=[('Jornada sin especificar', 'sin especificar'), ('Jornada Intensiva', 'intensiva'), ('Jornada Indiferente', 'flexible'), ('Jornada Parcial', 'parcial'), ('Jornada Fin de Semana', 'fin de semana'), ('Jornada Completa', 'completa'), ('Jornada Tele Trabajo', 'tele trabajo')], default='Sin especificar', max_length=30)),
                ('contract', models.CharField(choices=[('Contrato sin especificar', 'sin especificar'), ('Contrato Prácticas', 'prácticas'), ('Contrato Indefinido', 'indefinido'), ('Contrato Autónomo o freelance', 'autónomo o freelance'), ('Contrato Fijo discontinuo', 'fijo discontinuo'), ('Contrato Formativo', 'formativo'), ('Contrato De duración determinada', 'de duración determinada')], default='Contrato sin especificar', max_length=40)),
                ('cityname', django_mysql.models.ListCharField(models.CharField(max_length=100), blank=True, max_length=606, null=True, size=6)),
                ('provincename', models.CharField(blank=True, max_length=100, null=True)),
                ('countryname', models.CharField(max_length=30, null=True)),
                ('nationality', models.CharField(max_length=30)),
                ('first_publication_date', models.DateField(blank=True, default=None, null=True)),
                ('last_update_date', models.DateField(blank=True, default=None, null=True)),
                ('expiration_date', models.DateField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('functions', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('it_is_offered', models.TextField(blank=True, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('area', models.CharField(choices=[('Educación, formación', 'Educación, formación'), ('Tecnología e informática', 'Tecnología e informática'), ('Sanidad, salud y servicios sociales', 'Sanidad, salud y servicios sociales'), ('Medios, editorial y artes gráficas', 'Medios, editorial y artes gráficas'), ('Compras, logística y transporte', 'Compras, logística y transporte'), ('Administrativos y secretariado', 'Administrativos y secretariado'), ('Profesionales, artes y oficios', 'Profesionales, artes y oficios'), ('Telecomunicaciones', 'Telecomunicaciones'), ('Legal', 'Legal'), ('Internet', 'Internet'), ('Banca y seguros', 'Banca y seguros'), ('Calidad, I+D, PRL y medio ambiente', 'Calidad, I+D, PRL y medio ambiente'), ('Recursos humanos', 'Recursos humanos'), ('Comercial, ventas', 'Comercial, ventas'), ('Ingeniería y producción', 'Ingeniería y producción'), ('Atención al cliente', 'Atención al cliente'), ('Construcción e inmobiliaria', 'Construcción e inmobiliaria'), ('Hostelería, Turismo', 'Hostelería, Turismo'), ('Administración de Empresas', 'Administración de Empresas'), ('Marketing y comunicación', 'Marketing y comunicación')], max_length=40)),
                ('category_level', models.CharField(choices=[('Mandos', 'Mandos'), ('Empleados', 'Empleados'), ('Técnicos', 'Técnicos'), ('Dirección', 'Dirección'), ('Sin especificar', 'Sin especificar')], default='Sin especificar', max_length=20, null=True)),
                ('vacancies', models.PositiveIntegerField(blank=True, null=True)),
                ('registered_people', models.PositiveIntegerField(default=0)),
                ('vacancies_update', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('company', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='job.Company')),
                ('country', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='job.Country')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('province', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='job.Province')),
            ],
            options={
                'verbose_name': 'historical Job',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCompany',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.URLField(null=True)),
                ('description', models.TextField(null=True)),
                ('resume', models.CharField(blank=True, max_length=300, null=True)),
                ('city_name', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('offers', models.IntegerField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('city', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='job.City')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Company',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='community',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communities', to='job.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='job.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='job.Province'),
        ),
    ]
