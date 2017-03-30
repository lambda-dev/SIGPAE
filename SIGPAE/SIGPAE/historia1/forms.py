# -*- coding: utf-8 -*-
from django import forms
from .models import *
from django.forms.formsets import BaseFormSet
from django.forms import inlineformset_factory
from django.forms.formsets import formset_factory

# FORMULARIO: Reportes Globales
# Form para hacer la busqueda de los reportes globales
class ReportForm(forms.Form):
    CFM = 'Ciencias Físicas y Matemáticas'
    CSH = 'Ciencias Sociales y Humanidades'
    CB = 'Ciencias Biológicas'
    CTAI = 'Ciencias y Tecnologías Administrativas e Industriales'
    DEG ='Decanato de Estudios Generales'
    DET='Decanato de Estudios Tecnológicos'
    DEP='Decanato de Estudios de Postgrado'
    DEPR='Decanato de Estudios Profesionales'
    DF = '1'
    DQ = '2'
    DM = '3'
    DMP= '4'
    DCTI= '5'
    DCCE= '6'
    DEC= '7'
    DTFT='8'
    DCTE='9'
    DPS='10'
    DCM='11'
    DCT='12'
    DCTC='13'
    DLL='14'
    DCEA='15'
    DI='16'
    DFI='17'
    DCS='18'
    DDAAP='19'
    DPU='20'
    DBC='21'
    DEA='22'
    DBO='23'
    DTPBB='24'
    DTS='25'
    DTI='26'
    DFGCB='27'
    CCB='28'
    CCP='29'
    CFG='30'
    CCIU='31'
    CTIE='32'
    CTEE='33'
    CIPOE='34'
    CTHH='35'
    CAA='36'
    CCELCI='37'
    CATOE='38'
    CTMMA='39'
    CBA='40'
    CSHU='41'
    IT='42'
    CQ='43'
    CM='44'
    CBI='45'
    CF='46'
    CTIE='47'
    CTIEL='48'
    CIM='49'
    CIQ='50'
    CIC='51'
    CIG='52'
    CIMA='53'
    CIPOE='54'
    CTMMAIM='55'
    CIT='56'
    CA='57'
    CEU='58'
    CTH='59'
    CCE='60'

    DEPARTAMENTOS = (
        (CFM, ((DF, 'Departamento de Física'),
               (DQ, 'Departamento de Química'),
               (DM, 'Departamento de Mecánica'),
               (DMP, 'Departamento de Matemáticas Puras y Aplicadas'),
               (DCTI, 'Departamento de Computación y Tecnología de la Información'),
               (DCCE, 'Departamento de Cómputo Científico y Estadística'),
               (DEC, 'Departamento de Electrónica y Circuitos'),
               (DTFT, 'Departamento de Termodinámica y Fenómenos de Transferencia'),
               (DCTE, 'Departamento de Conversión y Transporte de Energía'),
               (DPS, 'Departamento de Procesos y Sistemas'),
               (DCM, 'Departamento de Ciencias de los Materiales'),
               (DCT, 'Departamento de Ciencias de la Tierra'),) ),
        (CSH, ((DCTC, 'Departamento de Ciencia y Tecnología del Comportamiento'),
               (DLL, 'Departamento de Lengua y Literatura'),
               (DCEA, 'Departamento de Ciencias Económicas y Administrativas'),
               (DI, 'Departamento de Idiomas'),
               (DFI, 'Departamento de Filosofía'),
               (DCS, 'Departamento de Ciencias Sociales'),
               (DDAAP, 'Departamento de Diseño Arquitectura y Artes Plásticas'),
               (DPU, 'Departamento de Planificación Urbana'),) ),
        (CB,  ((DBC, 'Departamento de Biología Celular'),
               (DEA, 'Departamento de Estudios Ambientales'),
               (DBO, 'Departamento de Biología de Organismos'),
               (DTPBB, 'Departamento de Tecnología de Procesos Biológicos y Bioquímicos'),) ),
        (CTAI,((DTS, 'Departamento de Tecnología de Servicios'),
               (DTI, 'Departamento de Tecnología Industrial'),
               (DFGCB, 'Departamento de Formación General y Ciencias Básicas'),) ),
        (DEG, ((CCB, 'Coordinación del Ciclo Básico'),
               (CCP, 'Coordinación del Ciclo Profesional'),
               (CFG, 'Coordinación de Formación General'),
               (CCIU, 'Coordinación del Ciclo de Iniciación Universitaria'),) ),
        (DET, ((CTIE, 'Coordinación de Tecnología e Ingeniería Eléctrica'),
               (CTEE, 'Coordinación de Tecnología Eléctrica y Electrónica'),
               (CIPOE, 'Coordinación de Ingeniería de Producción y Organización Empresarial'),
               (CTHH, 'Coordinación de Turismo, Hotelería y Hospitalidad'),
               (CAA, 'Coordinación de Administración Aduanera'),
               (CCELCI, 'Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional'),
               (CATOE, 'Coordinación de Administración del Transporte y Organización Empresarial'),
               (CTMMA, 'Coordinación de Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento'),) ),
        (DEP, ((CBA, 'Ciencias Básicas y Aplicadas'),
               (CSHU, 'Ciencias Sociales y Humanidades'),
               (IT, 'Ingeniería y Tecnología'),) ),
        (DEPR,((CQ, 'Coordinación de Química'),
               (CM, 'Coordinación de Matemática'),
               (CBI, 'Coordinación de Biología'),
               (CF, 'Coordinación de Física'),
               (CTIE, 'Coordinación de Tecnología e Ingeniería Eléctrica'),
               (CTIEL, 'Coordinación de Tecnología e Ingeniería Electrónica'),
               (CIM, 'Coordinación de Ingeniería Mecánica'),
               (CIQ, 'Coordinación de Ingeniería Química'),
               (CIC, 'Coordinación de Ingeniería de Computación'),
               (CIG, 'Coordinación de Ingeniería Geofísica'),
               (CIMA, 'Coordinación de Ingeniería de Materiales'),
               (CIPOE, 'Coordinación de Ingeniería de Producción y Organización Empresarial'),
               (CTMMAIM, 'Coordinación de Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento'),
               (CIT, ' Coordinación de Ingeniería de Telecomunicaciones'),
               (CA, 'Coordinación de Arquitectura'),
               (CEU, 'Coordinación de Estudios Urbanos'),
               (CTH, 'Coordinación de Turismo, Hotelería y Hospitalidad'),
               (CCE, 'Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional'),) )
    )

    departamento = forms.ChoiceField(
        choices=DEPARTAMENTOS
    )

    TIPOS = (
        ("PP", "Programas"),
        ("TT", "Transcripciones"),
        ("ALL", "Ambos")
    )
    tipo = forms.ChoiceField(
        choices = TIPOS
    )

# FORMULARIO: Por Aprobar
# Form para pedir los datos requeridos del usuario al guardar como Por Aprobar
class PASAForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['nombre', 'email', 'telefono']

# FORMULARIO: Subir PDF
# Form que permite subir los documentos PDF al sistema
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', 'scanned', )

        def __init__(self, *args, **kwargs):
            super(DocumentForm, self).__init__(*args, **kwargs)
            self.fields['description'].label = "Descripción:"
            self.fields['document'].label = "Documento A Subir:"
            self.fields['scanned'].label = "Utilizar Reconocimiento de Caracteres:"

# FORMULARIO: Guardar/Editar
# Form que muestra los datos de las Transcripciones y permite su edición y futuro guardado
class SaveForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['asignatura','codigo','creditos','fecha_vigano', 'fecha_vigtrim','departamento','requisitos','justificacion','objetivos','contenidos','metodologias','evaluacion','horas_teoria','horas_lab','horas_practica','guardar']
        
        def __init__(self, *args, **kwargs):
            super(SaveForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(SaveForm, self).clean()
        cod = cleaned_data.get("codigo")
        h_lab = cleaned_data.get("horas_lab")
        h_teo = cleaned_data.get("horas_teoria")
        h_prac = cleaned_data.get("horas_practica")
        creds = cleaned_data.get("creditos")
        year = cleaned_data.get("fecha_vigano")
        trim = cleaned_data.get("fecha_vigtrim")
        pasa = cleaned_data.get("guardar")
        asig = cleaned_data.get("asignatura")
        sinop = cleaned_data.get("contenidos")

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
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener Departamento válido")
            #horas teo, lab, prac
            if h_lab is None:
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener horas de laboratorio")
            if h_teo is None:
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener horas de teoría")
            if h_prac is None:
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener horas de práctica")
            if sinop == '':
                raise forms.ValidationError("Error: Para guardar como P.A.S.A. debe tener contenidos sinópticos")

# FORMULARIO: Buscar Transcripciones
# Form para hacer las consultas de las transcripciones guardadas en el sistema
class SearchForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['codigo', 'fecha_vigano', 'fecha_vigtrim']

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['codigo'].required = True
        self.fields['fecha_vigano'].required = False
        self.fields['fecha_vigtrim'].required = False

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        cod = cleaned_data.get("codigo")
        year = cleaned_data.get("fecha_vigano")
        trim = cleaned_data.get("fecha_vigtrim")

        if (year is None and trim != 'NN') or (year is not None and trim == 'NN'):
           raise forms.ValidationError("Trimeste y año deben tener valores o ser ambos vacios.")

# FORMULARIO: Buscar Programas
# Form para hacer las consultas de Programas guardados en SIGPAE
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

# FORMULARIO: Mostrar Programa
# Form para mostrar el contenido de los Programas, con los campos bloqueados
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

# FORMULARIO: Fuentes de Informacion
# Form para añadir nuevas fuentes de informacion
class RefForm(forms.ModelForm):
    class Meta:
        model = Referencia
        fields = ['titulo', 'document']

        def __init__(self, *args, **kwargs):
            super(RefForm, self).__init__(*args, **kwargs)
            self.fields['titulo'].required = True
            self.fields['titulo'].label = "Título"

# FORMULARIO: Autores
# Form para añadir nuevos autores a una fuente
class AutForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['name','apellido','referencia']

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

# FORMULARIO: Mostrar Por Aprobar
# Form para mostrar el contenido de los documentos Por Aprobar, con los campos bloqueados
class ViewPASAForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['nombre', 'email','telefono', 'asignatura','codigo','creditos','fecha_vigano', 'fecha_vigtrim','departamento','requisitos','objetivos','contenidos','metodologias','evaluacion','horas_teoria','horas_lab','horas_practica']

    def __init__(self, *args, **kwargs):
        super(ViewPASAForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].disabled = True
        self.fields['email'].disabled = True
        self.fields['telefono'].disabled = True
        self.fields['asignatura'].disabled = True
        self.fields['codigo'].disabled = True
        self.fields['creditos'].disabled = True
        self.fields['fecha_vigano'].disabled = True
        self.fields['fecha_vigtrim'].disabled = True
        self.fields['departamento'].disabled = True
        self.fields['requisitos'].disabled = True
        self.fields['objetivos'].disabled = True
        self.fields['metodologias'].disabled = True
        self.fields['evaluacion'].disabled = True
        self.fields['horas_teoria'].disabled = True
        self.fields['horas_lab'].disabled = True
        self.fields['horas_practica'].disabled = True

# FORMULARIO: Datos extra de Referencias
# Form para añadir datos extra a las referencias: editoria, etc
class FormDatosRef(forms.ModelForm):
    class Meta:
        model = DatosReferencia
        fields = ['editorial','edicion','year_r','nota', 'referencia']

# FORMULARIO: Campos Extra
# Form para añadir campos extra a una transcripcion
class ExtraFields(forms.ModelForm):
    class Meta:
        model = CamposExtra
        fields = ['nombre','value']

        def __init__(self, *args, **kwargs):
            super(ExtraFields, self).__init__(*args, **kwargs)
            self.fields['nombre'].required = False
            self.fields['value'].required = False
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
            try:
                title = form.cleaned_data['nombre']
                if title in titles:
                    raise forms.ValidationError("Los campos deben tener nombres distintos")
                titles.append(title)
            except:
                pass

