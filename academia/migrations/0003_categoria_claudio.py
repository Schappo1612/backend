# Generated by Django 4.2.5 on 2023-09-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0002_produtos_capa'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='claudio',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
