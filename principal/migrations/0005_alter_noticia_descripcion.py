# Generated by Django 3.2.4 on 2021-06-30 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20210629_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='descripcion',
            field=models.CharField(max_length=900, verbose_name='Contenido'),
        ),
    ]
