# Generated by Django 4.2.5 on 2023-09-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0004_alter_fornecedor_options_remove_fornecedor_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]