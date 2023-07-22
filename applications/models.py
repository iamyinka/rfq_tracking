import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from rfps.models import Rfp
from reps.models import Representative

STATUS_REVIEWED = ('REVIEWED', "Being Reviewed")
STATUS_APPROVED = ("APPROVED", "Approved")
STATUS_REJECTED = ("REJECTED", "Application Rejected")
STATUS_SUBMITTED = ("SUBMITTED", "Submitted")

STATUS = (
    STATUS_REVIEWED,
    STATUS_APPROVED,
    STATUS_REJECTED
)

class Application(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    rfp = models.ForeignKey(Rfp, on_delete=models.SET_NULL, null=True, related_name="rfp_applications")
    rep = models.ForeignKey(Representative, on_delete=models.SET_NULL, null=True, related_name="rep_applications")
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="approvals")
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="reviews")
    status = models.CharField(max_length=50, choices=STATUS, default=STATUS_SUBMITTED)
    concept_note = models.TextField(blank=True, null=True)
    submission_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rfp} -  {self.status}"
    

