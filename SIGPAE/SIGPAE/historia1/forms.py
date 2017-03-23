from django import forms
from .models import *
from django.forms.formsets import BaseFormSet
from django.forms import inlineformset_factory
from django.forms.formsets import formset_factory


class PASAForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['nombre', 'email', 'telefono']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', 'scanned', )

        def __init__(self, *args, **kwargs):
            super(DocumentForm, self).__init__(*args, **kwargs)
            self.fields['description'].label = "Descripción:"
            self.fields['document'].label = "Documento A Subir:"
            self.fields['scanned'].label = "Utilizar Reconocimiento de Caracteres:"

class SaveForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['asignatura','codigo','creditos','year', 'trimestre','fecha','departamento','requisitos','justificacion','objetivos','contenidos','metodologias','evaluacion','bibliografias','horas_teoria','horas_lab','horas_practica','guardar']
        
        def __init__(self, *args, **kwargs):
            super(SaveForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(SaveForm, self).clean()
        cod = cleaned_data.get("codigo")
        h_lab = cleaned_data.get("horas_lab")
        h_teo = cleaned_data.get("horas_teoria")
        h_prac = cleaned_data.get("horas_practica")
        creds = cleaned_data.get("creditos")
        year = cleaned_data.get("year")
        trim = cleaned_data.get("trimestre")
        pasa = cleaned_data.get("guardar")
        asig = cleaned_data.get("asignatura")
        fuentes = cleaned_data.get("bibliografias")
        sinop = cleaned_data.get("contenidos")
        print(cleaned_data)

        if h_lab is not None and h_teo is not None and h_prac is not None:
            if h_lab + h_teo + h_prac > 40:
                raise forms.ValidationError("Error: Suma de horas es mayor a 40")
        elif h_lab is not None and h_teo is not None:
            if h_lab + h_teo > 40:
                raise forms.ValidationError("Error: Suma de horas es mayor a 40")
        elif h_lab is not None and h_prac is not None:
            if h_lab + h_teo > 40:
                raise forms.ValidationError("Error: Suma de horas es mayor a 40")
        elif h_prac is not None and h_teo is not None:
            if h_prac + h_teo > 40:
                raise forms.ValidationError("Error: Suma de horas es mayor a 40")
        elif h_prac is not None:
            if h_prac > 40:
                raise forms.ValidationError("Error: Suma de horas es mayor a 40")
        elif h_teo is not None:
            if h_teo > 40:
                raise forms.ValidationError("Error: Suma de horas es mayor a 40")
        elif h_lab is not None:
            if h_lab > 40:
                raise forms.ValidationError("Error: Suma de horas es mayor a 40")

        if creds is not None:
            if (creds < 0) or (creds > 16):
                raise forms.ValidationError("Error: Valor de créditos fuera de rango")
        
        if (year is not None) and (year > 2017 or year < 1969):
            raise forms.ValidationError("Error: Valor del año inválido")

        # Validar que no exista un programa con mismo cod y per
        if (year is not None) and (trim != "NN"):
            progs = Programa.objects.all().filter(codigo=cod, fecha_vigtrim=trim, fecha_vigano=year)
            if progs.exists():
                raise forms.ValidationError("Error: Ya existe un programa en SIGPAE con el mismo código y período")

        print(cleaned_data)
        # Verificar que campos obligatorios no esten vacios
        if pasa == "PASA":
            if cod == '':
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener código")
            if asig == '':
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener denominación")
            #fecha/perido
            if year is None:
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener fecha")
            if trim == 'NN':
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener fecha")
            #horas teo, lab, prac
            if h_lab is None:
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener horas de laboratorio")
            if h_teo is None:
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener horas de teoría")
            if h_prac is None:
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener horas de práctica")
            if sinop == '':
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener contenidos sinópticos")
            if fuentes == '':
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener fuentes")

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
        fields = ['codigo','materia','creditos','h_teoria','h_prac','h_lab','fecha_vigano','fecha_vigtrim','obj_g','obj_e','contenidos', 'estrategias', 'estrat_eval', 'fuentes', 'cronograma', 'sinoptico']

    def __init__(self, *args, **kwargs):
        super(ViewProgForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].disabled = True
        self.fields['creditos'].disabled = True
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

class RefForm(forms.ModelForm):
    class Meta:
        model = Referencia
        fields = ['titulo','editorial','edicion']

        def __init__(self, *args, **kwargs):
            super(RefForm, self).__init__(*args, **kwargs)
            self.fields['titulo'].required = True
            self.fields['editorial'].required = True
            self.fields['edicion'].required = True
            self.fields['titulo'].label = "Titulo del libro"
            self.fields['editorial'].label = "Editorial del libro"
            self.fields['edicion'].label = "Edicion y/o año de vigencia"


class AutForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['name','apellido']

        def __init__(self, *args, **kwargs):
            super(AutForm, self).__init__(*args, **kwargs)
            self.fields['name'].required = True
            self.fields['apellido'].required = True
            self.fields['name'].label = "Nombre Autor"
            self.fields['apellido'].label = "Apellido Autor"

class BaseLinkFormSetR(BaseFormSet):
    def add_fields(self, form, index):
        super(BaseLinkFormSetR, self).add_fields(form, index)
        form.fields['Nombre Autor']= forms.CharField()
        form.fields['Apellido Autor']= forms.CharField()

class ViewPASAForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['nombre', 'email','telefono', 'asignatura','codigo','creditos','year', 'trimestre','departamento','requisitos','objetivos','contenidos','metodologias','evaluacion','bibliografias','horas_teoria','horas_lab','horas_practica']

    def __init__(self, *args, **kwargs):
        super(ViewPASAForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].disabled = True
        self.fields['email'].disabled = True
        self.fields['telefono'].disabled = True
        self.fields['asignatura'].disabled = True
        self.fields['codigo'].disabled = True
        self.fields['creditos'].disabled = True
        self.fields['year'].disabled = True
        self.fields['trimestre'].disabled = True
        self.fields['departamento'].disabled = True
        self.fields['requisitos'].disabled = True
        self.fields['objetivos'].disabled = True
        self.fields['metodologias'].disabled = True
        self.fields['evaluacion'].disabled = True
        self.fields['bibliografias'].disabled = True
        self.fields['horas_teoria'].disabled = True
        self.fields['horas_lab'].disabled = True
        self.fields['horas_practica'].disabled = True

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
            if 'nombre' in form.cleaned_data:
                title = form.cleaned_data['nombre']
                if title in titles:
                    raise forms.ValidationError("Los campos deben tener nombres distintos")
                titles.append(title)

