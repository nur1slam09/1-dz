# Generated by Django 5.0.6 on 2024-05-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_image/', verbose_name='Фото')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('desc', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
    ]