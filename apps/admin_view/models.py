from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
