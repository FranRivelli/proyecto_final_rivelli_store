# Generated by Django 5.1.3 on 2024-12-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0007_rename_cliente_clientes_rename_vendedor_vendedores'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vendedores',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]