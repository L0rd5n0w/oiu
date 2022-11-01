from email.policy import default
from django.db import models

# Create your models here.

class Dane(models.Model):
    slackUsername = models.CharField(max_length=100)
    backend = models.BooleanField(default=True)
    age = models.IntegerField(null=True)
    bio = models.CharField(max_length=400)


    def __str__(self):
        return self.slackUsername









