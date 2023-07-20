from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Representative
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_representative(sender, instance, created, **kwargs):
    if created:
        Representative.objects.create(user=instance)