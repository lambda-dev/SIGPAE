from django import forms
from .models import Document
from .models import Transcripcion

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')

class TranscripcionForm(forms.ModelForm):
    class Meta:
        model = Transcripcion
        fields = ('periodo', 'year')
