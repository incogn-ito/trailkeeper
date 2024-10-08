from django.forms import ModelForm
from .models import Step

class StepForm(ModelForm):
  class Meta:
    model = Step
    fields = ['date', 'path', 'description']