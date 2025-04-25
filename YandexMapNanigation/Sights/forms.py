from django import forms
from .models import Sight


class SightForm(forms.ModelForm):
    
    class Meta:
        model = Sight
        fields = ('title', 'description', 'latitude', 'longitude')