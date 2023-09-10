# Generated by Django 4.2.5 on 2023-09-09 22:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnos',
            name='Horario',
        ),
        migrations.AddField(
            model_name='profesional_salud',
            name='Nro_telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turnos',
            name='fecha',
            field=models.CharField(choices=[('2023-09-10', '10 de Septiembre de 2023'), ('2023-09-11', '11 de Septiembre de 2023'), ('2023-09-12', '12 de Septiembre de 2023'), ('2023-09-13', '13 de Septiembre de 2023'), ('2023-09-14', '14 de Septiembre de 2023'), ('2023-09-15', '15 de Septiembre de 2023'), ('2023-09-16', '16 de Septiembre de 2023'), ('2023-09-17', '17 de Septiembre de 2023'), ('2023-09-18', '18 de Septiembre de 2023'), ('2023-09-19', '19 de Septiembre de 2023'), ('2023-09-20', '20 de Septiembre de 2023'), ('2023-09-21', '21 de Septiembre de 2023'), ('2023-09-22', '22 de Septiembre de 2023'), ('2023-09-23', '23 de Septiembre de 2023'), ('2023-09-24', '24 de Septiembre de 2023'), ('2023-09-25', '25 de Septiembre de 2023'), ('2023-09-26', '26 de Septiembre de 2023'), ('2023-09-27', '27 de Septiembre de 2023'), ('2023-09-28', '28 de Septiembre de 2023'), ('2023-09-29', '29 de Septiembre de 2023'), ('2023-09-30', '30 de Septiembre de 2023'), ('2023-10-01', '1 de octubre de 2023')], default=django.utils.timezone.now, max_length=10),
        ),
        migrations.AddField(
            model_name='turnos',
            name='profesional',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appWeb.profesional_salud'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Turnosprofesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appWeb.profesional_salud')),
                ('turnos_designados', models.ManyToManyField(to='appWeb.turnos')),
            ],
        ),
        migrations.CreateModel(
            name='Turnospaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appWeb.paciente')),
                ('turnos_Adquiridos', models.ManyToManyField(to='appWeb.turnos')),
            ],
        ),
        migrations.AddField(
            model_name='turnos',
            name='horario',
            field=models.CharField(choices=[('09:00', '9:00 AM'), ('09:30', '9:30 AM'), ('10:00', '10:00 AM'), ('10:30', '10:30 AM'), ('11:00', '11:00 AM'), ('11:30', '11:30 AM'), ('12:00', '12:00 AM'), ('12:30', '12:30 AM')], default=django.utils.timezone.now, max_length=5),
        ),
    ]