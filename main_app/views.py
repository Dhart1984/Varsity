from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Player
from .forms import ScheduleForm


# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')


@login_required
def players_index(request):
    players = Player.objects.filter(user=request.user)
    return render(request, 'players/index.html', { 'players' : players})


@login_required
def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  schedule_form = ScheduleForm()
  print (player)
  return render(request, 'players/detail.html', { 'player': player, 'schedule_form' : schedule_form})

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'age', 'lifetime_ba',]
    
    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ['name', 'age', 'lifetime_ba',]

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players'

