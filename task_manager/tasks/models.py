from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('DONE', 'Done'),
    ]

    PERIOD_CHOICES = [
        ('MORNING', 'Morning'),
        ('NOON', 'Noon'),
        ('NIGHT', 'Night'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='MORNING')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        ordering = ['status', 'due_date', 'title']

    def __str__(self):
        return self.title
