# Generated by Django 3.2.4 on 2021-07-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_remove_noticia_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.CharField(default='', max_length=100),
        ),
    ]
