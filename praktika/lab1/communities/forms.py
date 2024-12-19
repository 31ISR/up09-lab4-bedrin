from django import forms 
from . import models 
from .models import Community

class CreateCommunity(forms.ModelForm): 
    class Meta: 
        model = models.Community
        fields = ['name','description','avatar']

class CommunityCreationForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description', 'avatar']
        