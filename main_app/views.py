from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import Player
from .forms import ScheduleForm


# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')



def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', { 'players' : players})



def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  schedule_form = ScheduleForm()
  print (player)
  return render(request, 'players/detail.html', { 'player': player, 'schedule_form' : schedule_form})

def add_schedule(request, player_id):
  # create a ModelForm instance using the data in request.POST
  form = ScheduleForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_schedule = form.save(commit=False)
    new_schedule.player_id = player_id
    new_schedule.save()
    return redirect('detail', player_id=player_id)



class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'age', 'lifetime_ba',]

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players'

