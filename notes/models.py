from django.db import models

# Create your models here.
from django.db import models

class Note (models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    color = models.CharField(max_length=7, default='#FFFFFF')  # Default white color
    created_time = models.DateTimeField(auto_now_add=True)
    custom_parameter = models.JSONField(blank=True, null=True)  # Requires Django 3.1+

    def __str__(self):
        return self.title
