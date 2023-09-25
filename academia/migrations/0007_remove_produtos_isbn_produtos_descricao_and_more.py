# Generated by Django 4.2.5 on 2023-09-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0006_rename_capa_produtos_imagem_remove_categoria_claudio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='isbn',
        ),
        migrations.AddField(
            model_name='produtos',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
