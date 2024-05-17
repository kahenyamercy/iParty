from django.db import models

class Campus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    initials = models.CharField(max_length=10)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
