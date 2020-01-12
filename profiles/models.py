from django.db import models
from django.contrib.auth.models import User

ch_status = (
    ("Open", "Open"),
    ("Busy", "Busy"),
)

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    bio = models.TextField(blank=True)

    linkedin_link = models.CharField(max_length=128, blank=True)
    github_link = models.CharField(max_length=128, blank=True)

    status = models.CharField(max_length=64, choices=ch_status, default = "Open")

    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        if self.first_name == '':
            return "Profile In Progress, {}".format(self.email)
        else:
            return "{0}, {1} : {2}" .format(self.first_name, self.last_name, self.email)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    bio = models.TextField(blank=True)

    company_name = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=64, blank=True)
    website = models.CharField(max_length=128, blank=True)

    def __str__(self):
        if self.first_name == '':
            return "Profile In Progress, {}".format(self.email)
        else:
            return "{0}, {1} : {2}".format(self.first_name, self.last_name, self.email)
