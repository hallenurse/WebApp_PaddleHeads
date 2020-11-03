from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Roster(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField()
    profile = models.TextField()
    batting_average = models.DecimalField(max_digits=4, decimal_places=3)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('roster_detail',args=[str(self.id)])

