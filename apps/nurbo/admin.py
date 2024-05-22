from django.contrib import admin

from apps.nurbo import models
# Register your models here.

admin.site.register(models.About)
admin.site.register(models.Academic)

