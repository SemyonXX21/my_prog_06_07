# Generated by Django 3.2.4 on 2021-07-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_ourdt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lucoshko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('telephone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('product', models.CharField(max_length=100, verbose_name='Продукт')),
                ('quantity', models.CharField(max_length=100, verbose_name='Количество')),
            ],
        ),
    ]
