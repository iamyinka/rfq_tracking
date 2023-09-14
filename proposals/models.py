import uuid
from django.db import models
from django.contrib.auth.models import User
from applications.models import Application

class Proposal(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    application = models.OneToOneField(Application, on_delete=models.SET_NULL, null=True)
    # responsible_person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prop_admins')
    responsible_person = models.CharField(max_length=255, blank=True, null=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prop_reviewers')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prop_reviewers')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prop_approvals')
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prop_submissions')
    amt_requested = models.DecimalField(max_digits=20, decimal_places="2")
    amt_awarded = models.DecimalField(max_digits=20, decimal_places="2", blank=True, null=True)
    award_date = models.DateField(blank=True, null=True)
    outcome = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.application