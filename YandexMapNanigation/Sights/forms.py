from django import forms
from .models import Sight


class SightForm(forms.ModelForm):
    
    class Meta:
        model = Sight
        fields = ('title', 'description', 'city', 'street', 'house_number', 'category')