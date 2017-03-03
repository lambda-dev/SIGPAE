from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'scanned', )

        def __init__(self, *args, **kwargs):
            super(RegistrationFormTOS, self).__init__(*args, **kwargs)
            self.fields['description'].label = "Descripción:"
            self.fields['document'].label = "Documento A Subir:"
            self.fields['scanned'].label = "Utilizar Reconocimiento de Caracteres:"


class SaveForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['asignatura','codigo','creditos','departamento','requisitos','objetivos','contenidos','metodologias','evaluacion','bibliografias','horas_teoria','fecha','horas_lab','horas_practica']
