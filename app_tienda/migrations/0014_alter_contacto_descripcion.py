# Generated by Django 5.1.3 on 2024-12-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0013_alter_contacto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
