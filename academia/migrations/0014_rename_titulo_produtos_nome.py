# Generated by Django 4.2.6 on 2023-11-27 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0013_alter_compra_status_alter_compra_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtos',
            old_name='titulo',
            new_name='nome',
        ),
    ]