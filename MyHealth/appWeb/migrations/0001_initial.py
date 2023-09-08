# Generated by Django 4.2.5 on 2023-09-08 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('DNI', models.IntegerField()),
                ('fecha_de_nacimiento', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('direccion', models.CharField(max_length=150)),
                ('Nro_telefono', models.IntegerField()),
                ('ocupacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional_salud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('DNI', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('nro_matricula', models.IntegerField()),
                ('especialidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Horario', models.DateTimeField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appWeb.paciente')),
            ],
        ),
    ]
