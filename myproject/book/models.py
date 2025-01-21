# models.py
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.FloatField()

    def get_rating_category(self):
        if self.rating < 1000:
            return "Baja"
        elif 1000 <= self.rating <= 2500:
            return "Media"
        else:
            return "Alta"

    def __str__(self):
        return f"{self.title} - {self.author}"

# Señal para crear los permisos automáticamente
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_custom_permissions(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(Book)
    Permission.objects.get_or_create(codename='development', name='Can manage development tasks', content_type=content_type)
    Permission.objects.get_or_create(codename='scrum_master', name='Can manage scrum tasks', content_type=content_type)
