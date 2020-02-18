from django import forms

from . import models
from .models import Song



class CreateFact(forms.Form):
    artist = forms.CharField(max_length=100, label='אומן')
    # date = forms.DateField(label='תאריך')
    song = forms.CharField(max_length=100, label='שיר')
    # songs = forms.ModelChoiceField(queryset=Song.objects.order_by('name'), label='בחר שיר')
    fact = forms.CharField(widget=forms.Textarea(), label='תיאור')
