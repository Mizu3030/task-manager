from django.db import models

class Task(models.Model):
    PERIOD_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
