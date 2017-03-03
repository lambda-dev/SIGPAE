from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class SaveForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['asignatura','codigo','creditos','departamento','requisitos','objetivos','contenidos','metodologias','evaluacion','bibliografias','horas_teoria','horas_lab','horas_practica','year', 'trimestre']
