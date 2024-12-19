# Generated by Django 5.1.3 on 2024-12-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0002_vendedor_producto_clase_de_producto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('tipo_cliente', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Otros_Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('vendedor', models.CharField(max_length=30)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('talle', models.CharField(max_length=5)),
                ('vendedor', models.CharField(max_length=30)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zapatillas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('talle', models.IntegerField()),
                ('vendedor', models.CharField(max_length=30)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]