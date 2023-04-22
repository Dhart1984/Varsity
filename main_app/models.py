from django.db import models
from django.urls import reverse

# tuples
EVENTS = (
    ('A', 'Practice'),
    ('B', 'Game'),
)


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    lifetime_ba = models.IntegerField()
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})
    
class Schedule(models.Model):
    date = models.DateField('Game or Practice date')
    event = models.CharField(max_length=1, choices=EVENTS, default=EVENTS[0][0])
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_event_display()} on {self.date}"