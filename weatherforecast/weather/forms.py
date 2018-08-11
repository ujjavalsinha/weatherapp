
from django import forms
from weather.models import City

class CityForm(forms.ModelForm):
    class Meta():
        model = City
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
        }
