from django import forms
from django.forms import ModelForm
from .models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['id', 'defineday', 'write']
        labels = {'defineday': 'Mood'}
        widgets = {'write': forms.Textarea(attrs={'class': 'form-control'})
        }