# Generated by Django 4.2.5 on 2023-09-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0003_alter_produtos_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='Fornecedor',
        ),
        migrations.AddField(
            model_name='produtos',
            name='Fornecedor',
            field=models.ManyToManyField(related_name='produtos', to='academia.fornecedor'),
        ),
    ]