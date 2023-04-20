from django.db import models
from django.urls import reverse

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    schedule = models.CharField(max_length=75)
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})