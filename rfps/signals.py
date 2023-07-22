from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Rfp
from django.core.mail import send_mail

@receiver(post_save, sender=Rfp)
def rfp_create_send_email(sender, instance, created, **kwargs):
    if created:
        recievers = []
        for user in User.objects.all():
            recievers.append(user.email)
        send_mail(
            "New RFP added to your dashboard",
            f"You have a new RFP in your dashboard that needs to be looked at.",
            "info@damienbelgium.be",
            [recievers],
            fail_silently=False,
        )