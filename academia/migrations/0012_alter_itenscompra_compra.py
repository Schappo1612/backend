# Generated by Django 4.2.6 on 2023-10-15 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0011_itenscompra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itenscompra',
            name='compra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='academia.compra'),
        ),
    ]
