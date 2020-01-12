from django.db import models
from profiles.models import Client, Consultant

ch_status = (
    ('Open', 'Open'),
    ('In Progress', 'In Progress'),
    ('Closed', 'Closed')
)

class Contract(models.Model):
    title = models.CharField(max_length=128)
    summary = models.TextField(blank=True)
    salary = models.CharField(max_length=128)

    skills = models.TextField(blank=True)
    jobTags = models.TextField(blank=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    applicants = models.ManyToManyField(Consultant, blank=True, related_name="applicants")
    team = models.ManyToManyField(Consultant, blank=True, related_name="team")

    status = models.CharField(max_length=64, choices=ch_status)

    def __str__(self):
        return self.title
