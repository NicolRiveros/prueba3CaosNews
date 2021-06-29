# Generated by Django 3.2.4 on 2021-06-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(max_length=100, verbose_name='Nombre categoria'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='descripcion',
            field=models.CharField(max_length=300, verbose_name='Informacion'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]