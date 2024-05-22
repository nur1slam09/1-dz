from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(
        upload_to='about_image/',
        verbose_name='Фото'
        )
    name = models.CharField(
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
        
class Academic(models.Model):
    profession = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    university = models.CharField(
        verbose_name ='Универсиет',
        max_length=255
    )
    def __str__(self):
        return self.profession
    
    class Meta:
        verbose_name = 'Академическая должность'
        verbose_name_plural = 'Академические должности'     
        

    
    


