# Generated by Django 4.1.7 on 2023-07-18 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario_ICED', '0006_sanciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamos',
            old_name='Pres_Equipos_id',
            new_name='Pres_Equipos_id_id',
        ),
        migrations.RenameField(
            model_name='prestamos',
            old_name='Pres_Usuarios_Documento',
            new_name='Pres_Usuarios_Documento_id',
        ),
    ]
