# Generated by Django 3.2.4 on 2021-07-01 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_alter_noticia_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.CharField(default='', max_length=100),
        ),
    ]
