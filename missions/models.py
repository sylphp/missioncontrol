from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Mission(models.Model):
    client = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    details = models.TextField()
    deliverables = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    selected_date = models.DateTimeField(
            blank=True, null=True)
    approved_date = models.DateTimeField(
            blank=True, null=True)
    finished_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title