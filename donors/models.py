import uuid
from django.db import models
from django_countries.fields import CountryField

class Donor(models.Model):
    FREQUENT_FIVE = ('FIVE', "5 Years")
    FREQUENT_THREE = ('THREE', "3 Years")
    FREQUENT_THREE_TIMES = ('THREEPLUS', "3 times a year")
    FREQUENT_GRANT_ANNOUNCEMENT = ("GA", "Grant Announcement")
    FREQUENT_ANNUAL = ("ONE", "Annually")
    FREQUENT_ALWAYS = ("ALWAYS", "Frequently")
    FREQUENT_ANYTIME = ("ANYTIME", "Submission is possible at any time")

    PROCESS_SUBMISSION = ("SP", "Submission of proposal")
    PROCESS_RFPLOI = ("RFPLOI", "RFP - LOI followed by full proposal")
    PROCESS_UNSOLICITEDRFP = ("UNSOLICITEDRFP", "Unsolicited & RFP")
    PROCESS_PROPOSAL = ("PROPOSAL", "Proposal")
    PROCESS_UNSOLICITED = ("UNSOLICITED", "Unsolicited")
    PROCESS_LOI = ("LOI", "LOI followed by full proposal")

    FREQUENCY = (
        FREQUENT_FIVE,
        FREQUENT_THREE_TIMES,
        FREQUENT_GRANT_ANNOUNCEMENT,
        FREQUENT_ANNUAL,
        FREQUENT_ALWAYS,
        FREQUENT_ANYTIME
    )

    PROCESSES = (
        PROCESS_SUBMISSION,
        PROCESS_RFPLOI,
        PROCESS_UNSOLICITEDRFP,
        PROCESS_PROPOSAL,
        PROCESS_UNSOLICITED,
        PROCESS_LOI,
    )

    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    country = CountryField()
    area_of_work = models.TextField(max_length=500, blank=True, null=True)
    eligible_countries = CountryField(multiple=True)
    frequency = models.CharField(max_length=150, choices=FREQUENCY)
    avg_funding = models.CharField(max_length=100)
    process_of_funding = models.CharField(max_length=200, choices=PROCESSES)
    df_funded = models.BooleanField(default=False)
    donors_url = models.URLField()
    contact = models.CharField(max_length=255)
