# Generated by Django 4.2.5 on 2023-09-25 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0007_remove_produtos_isbn_produtos_descricao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='imagem',
        ),
    ]
