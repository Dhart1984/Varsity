from django.db import models
from django.urls import reverse

# tuples
SPORTS = (
    ('A', 'Practice'),
    ('B', 'Game'),
)


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    schedule = models.CharField(max_length=75)
   

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})
    
class Sport(models.Model):
    team = models.CharField(max_length=75)
    coach = models.CharField(max_length=75)
    date = models.DateField('Game or Practice date')
    contact = models.CharField(max_length=75)
    sports = models.CharField(max_length=1, choices=SPORTS, default=SPORTS[0][0])
    


    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_sports_display()} on {self.date}"