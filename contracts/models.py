from django.db import models

ch_status = (
    ('Open', 'Open'),
    ('In Progress', 'In Progress'),
    ('Closed', 'Closed')
)

class Contracts(models.Model):
    title = models.CharField(max_length=128)
    summary = models.TextField(blank=True)
    salary = models.CharField(max_length=128, blank=True)

    skills = models.TextField(blank=True)
    jobTags = models.TextField(blank=True)

    client = models.CharField(max_length=128)
    applicants = models.TextField(blank=True)
    team = models.TextField(blank=True)

    status = models.CharField(max_length=64, choices=ch_status)

    def __str__(self):
        return self.title
