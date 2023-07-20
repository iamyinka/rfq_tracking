import uuid
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Representative(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=150)
    country = CountryField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username