# Generated by Django 2.2.7 on 2019-12-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20191221_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.CharField(default='', max_length=50, verbose_name='Imdb'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='turu',
            field=models.CharField(default='', max_length=100, verbose_name='Sort'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='yil',
            field=models.CharField(default='', max_length=50, verbose_name='Year'),
        ),
    ]
