from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
class Schedule(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    opponent = models.TextField()
    location = models.TextField()
    promotion = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('schedule_detail', args=[str(self.id)])
