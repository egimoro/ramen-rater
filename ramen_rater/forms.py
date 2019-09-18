from django.forms import ModelForm
from .models import Ramen
from django import forms


class RamenForm(ModelForm):
    class Meta:
        model = Ramen
        fields = '__all__'





        