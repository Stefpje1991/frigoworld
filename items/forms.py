from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['naam', 'beschrijving', 'prijs', 'beschikbaar', 'categorie', 'inhoud', 'foto']