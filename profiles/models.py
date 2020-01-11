from django.db import models

ch_status = (
    ("Open", "Open"),
    ("Busy", "Busy"),
)

# Create your models here.
class Consultant(models.Model):
    first_name = models.Charfield(max_length = 64)
    last_name = models.Charfield(max_length = 64)
    email = models.Charfield(max_length = 64)
    bio = models.Textfield(max_length = 64)

    linkedin_link = models.Charfield(max_length = 128)
    github_link = models.Charfield(max_length = 128)

    status = models.Charfield(max_length = 64, choices=ch_status, default = "Open")

    job_tags = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    previous_contracts = models.TextField(blank=True)

    def __str__(self):
        #How objects of this class will appear in admin pannel
        return "{0},{1} : {2}" .format(self.first_name, self.last_name, self.email)

class Client(models.Model):
    first_name = models.Charfield(max_length = 64)
    last_name = models.Charfield(max_length = 64)
    email = models.Charfield(max_length = 64)

    website = models.Charfield(max_length = 128)
    job_tags = models.TextField(blank=True)

    def __str__(self):
        #How objects of this class will appear in admin pannel
        return "{0},{1} : {2}" .format(self.first_name, self.last_name, self.email)
