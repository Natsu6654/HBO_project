# Generated by Django 5.1 on 2024-11-08 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hbomovietalk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
