from django.db import models

# Create your models here.
class Works(models.Model):
    work = models.ImageField(
        upload_to='about_image/',
        verbose_name='Фото'
        )
    educationofOne = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='О нас'
        verbose_name_plural='О нас'