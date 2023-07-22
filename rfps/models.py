import uuid
from django.db import models
from django.contrib.auth.models import User
from donors.models import Donor
from django_countries.fields import CountryField

class Rfp(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='rfps')
    call_type = models.CharField(max_length=255)
    grant_value = models.CharField(max_length=200, blank=True, null=True)
    advert_date = models.DateField()
    closing_date = models.DateField()
    eligible_countries = CountryField(multiple=True)
    concept_note = models.FileField(blank=True, null=True)
    submission_date = models.DateField()
    applicants = models.TextField(default='', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.donor} - {self.call_type}"

    

