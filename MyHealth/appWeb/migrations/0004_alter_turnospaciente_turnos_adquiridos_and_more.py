# Generated by Django 4.2.5 on 2023-09-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0003_profesionalsalud_alter_paciente_dni_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnospaciente',
            name='turnos_Adquiridos',
            field=models.ManyToManyField(to='appWeb.turnos', verbose_name='Turnos adquiridos'),
        ),
        migrations.AlterField(
            model_name='turnosprofesional',
            name='turnos_designados',
            field=models.ManyToManyField(to='appWeb.turnos', verbose_name='Turnos designados'),
        ),
    ]