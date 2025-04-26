from django import forms
from .models import Sight, Rating


class SightForm(forms.ModelForm):
    
    class Meta:
        model = Sight
        fields = ('title', 'description', 'city', 'street', 'house_number', 'category')


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('rating', 'comment')
