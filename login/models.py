from django.db import models
from django.contrib.auth.models import User

ch_type = (
    ('Consultant', 'Consultant'),
    ('Client', 'Client')
)

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=32, choices=ch_type, blank=True)

    def __str__(self):
        return "{}".format(self.user.username)
