from django.forms import ModelForm
from .models import Bet

class BetForm(ModelForm):
    class Meta:
        model = Bet
        fields= '__all__'






