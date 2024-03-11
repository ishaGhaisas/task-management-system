from django.db import models

class Tasks(models.Model):
    taskName = models.CharField(max_length=255)