from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    initials = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.initials