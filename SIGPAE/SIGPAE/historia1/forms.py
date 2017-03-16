from django import forms
from django.forms.formsets import BaseFormSet
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'scanned', )

        def __init__(self, *args, **kwargs):
            super(DocumentForm, self).__init__(*args, **kwargs)
            self.fields['description'].label = "Descripción:"
            self.fields['document'].label = "Documento A Subir:"
            self.fields['scanned'].label = "Utilizar Reconocimiento de Caracteres:"

class SaveForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['asignatura','codigo','creditos','departamento','requisitos','objetivos','contenidos','metodologias','evaluacion','bibliografias','horas_teoria','horas_lab','horas_practica','year', 'trimestre','justificacion']

        def __init__(self, *args, **kwargs):
            super(SaveForm, self).__init__(*args, **kwargs)

class SearchForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['codigo', 'year', 'trimestre']

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].required = True
        self.fields['year'].required = False
        self.fields['trimestre'].required = False

class ExtraFields(forms.ModelForm):

    class Meta:
        model = CamposExtra
        fields = ['nombre','value']

        def __init__(self, *args, **kwargs):
            super(ExtraFields, self).__init__(*args, **kwargs)
            self.fields['nombre'].required = True
            self.fields['value'].required = True
            self.fields['nombre'].label = "Nombre:"
            self.fields['value'].label = "Texto:"

class BaseLinkFormSet(BaseFormSet):
    def clean(self):
        """Checks that no two articles have the same title."""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return
        titles = []
        for form in self.forms:
            title = form.cleaned_data['nombre']
            if title in titles:
                raise forms.ValidationError("Los campos deben tener nombres distintos")
            titles.append(title)
