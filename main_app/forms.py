# forms.py

from django.forms import ModelForm
from .models import Sport

class SportForm(ModelForm):
  class Meta:
    model = Sport
    fields = ['sports', "date"]
