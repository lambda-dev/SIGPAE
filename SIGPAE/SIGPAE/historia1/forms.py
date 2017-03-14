from django import forms
from .models import Document, Programa

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
        fields = ['asignatura','codigo','creditos','departamento','requisitos','objetivos','contenidos','metodologias','evaluacion','bibliografias','horas_teoria','horas_lab','horas_practica','year', 'trimestre']

    def clean(self):
        cleaned_data = super(SaveForm, self).clean()
        cod = cleaned_data.get("codigo")
        # Revisar si suma de horas no da > 40

class SearchForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['codigo', 'year', 'trimestre']

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].required = True
        self.fields['year'].required = False
        self.fields['trimestre'].required = False

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        cod = cleaned_data.get("codigo")
        year = cleaned_data.get("year")
        trim = cleaned_data.get("trimestre")

        if (year is None and trim != 'NN') or (year is not None and trim == 'NN'):
           raise forms.ValidationError("Trimeste y año deben tener valores o ser ambos vacios.")

class SearchFormProg(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['codigo', 'fecha_vigano', 'fecha_vigtrim']

    def __init__(self, *args, **kwargs):
        super(SearchFormProg, self).__init__(*args, **kwargs)
        self.fields['codigo'].required = True
        self.fields['fecha_vigano'].required = False
        self.fields['fecha_vigtrim'].required = False

    def clean(self):
        cleaned_data = super(SearchFormProg, self).clean()
        cod = cleaned_data.get("codigo")
        year = cleaned_data.get("fecha_vigano")
        trim = cleaned_data.get("fecha_vigtrim")

        if (year is None and trim != 'NN') or (year is not None and trim == 'NN'):
            raise forms.ValidationError("Trimeste y año deben tener valores o ser ambos vacios.")

class ViewProgForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['codigo','materia','h_teoria','h_prac','h_lab','fecha_vigano','fecha_vigtrim','obj_g','obj_e','contenidos', 'estrategias', 'estrat_eval', 'fuentes', 'cronograma', 'sinoptico']

    def __init__(self, *args, **kwargs):
        super(ViewProgForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].disabled = True
        self.fields['materia'].disabled = True
        self.fields['h_teoria'].disabled = True
        self.fields['h_prac'].disabled = True
        self.fields['h_lab'].disabled = True
        self.fields['fecha_vigano'].disabled = True
        self.fields['fecha_vigtrim'].disabled = True
        self.fields['sinoptico'].disabled = True
        self.fields['contenidos'].disabled = True
        self.fields['estrategias'].disabled = True
        self.fields['estrat_eval'].disabled = True
        self.fields['fuentes'].disabled = True
        self.fields['cronograma'].disabled = True

