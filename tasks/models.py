from django.utils import timezone
from django.db import models


class Tasks(models.Model):
    taskName = models.CharField(max_length=255)
    description = models.CharField(blank=True, null=True,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)    
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='medium')
    status = models.CharField(max_length=20, choices=[
        ('in_progress', 'In Progress'),
        ('to-do', 'To Do'),
        ('completed', 'Completed'),
        ('blocked', 'Blocked')
    ], default='to-do')
    # TODO
    # assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    # project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    # tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.taskName