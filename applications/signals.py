# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Application

# @receiver(post_save, sender=Application)
# def add_reps_to_applications(sender, instance, created, **kwargs):
#     if created:
#         reps = set()
#         reps.add(instance.rep.user.username)
#         for rep in reps:
#             instance.applicants += f"{rep},"
#             instance.applicants.rstrip(",")
#             instance.save()
        