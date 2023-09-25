# Generated by Django 4.2.5 on 2023-09-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0003_categoria_claudio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedor',
            options={},
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='email',
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='claudio',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
