from django import forms
from django.forms import ModelForm
from .models import IndividualArt, User

class UploadArt(ModelForm):
    class Meta:
        model = IndividualArt
        fields = '__all__'

class UpdateArt(ModelForm):
    class Meta:
        model = IndividualArt
        fields = ['artPiece', 'title', 'description']