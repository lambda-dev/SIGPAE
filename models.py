from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Student(models.Model):
    CFM = 'Ciencias Físicas y Matemáticas'
    CSH = 'Ciencias Sociales y Humanidades'
    CB = 'Ciencias Biológicas'
    CTAI = 'Ciencias y Tecnologías Administrativas e Industriales'
    DEG ='Decanato de Estudios Generales'
    DET='Decanato de Estudios Tecnológicos'
    DEP='Decanato de Estudios de Postgrado'
    DEPR='Decanato de Estudios Profesionales'
    DF = 1
    DQ = 2
    DM = 3
    DMP=4
    DCTI=5
    DCCE=6
    DEC=7
    DTFT=8
    DCTE=9
    DPS=10
    DCM=11
    DCT=12
    DCTC=13
    DLL=14
    DCEA=15
    DI=16
    DFI=17
    DCS=18
    DDAAP=19
    DPU=20
    DBC=21
    DEA=22
    DBO=23
    DTPBB=24
    DTS=25
    DTI=26
    DFGCB=27
    CCB=28
    CCP=29
    CFG=30
    CCIU=31
    CTIE=32
    CTEE=33
    CIPOE=34
    CTHH=35
    CAA=36
    CCELCI=37
    CATOE=38
    CTMMA=39
    CBA=40
    CSHU=41
    IT=42
    CQ=43
    CM=44
    CBI=45
    CF=46
    CTIE=47
    CTIEL=48
    CIM=49
    CIQ=50
    CIC=51
    CIG=52
    CIMA=53
    CIPOE=54
    CTMMAIM=55
    CIT=56
    CA=57
    CEU=58
    CTH=59
    CCE=60

    YEAR_IN_SCHOOL_CHOICES = (
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
               (CCE, 'Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional'),) ),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        #choices.size=10,
        default=DCT,
        #size= 10,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
