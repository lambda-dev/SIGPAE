import re

departamentos={	'CO':'Computo Cientifico y Estadistico',
				'EP':'Cursos en Cooperación',
				'ET':'Cursos en Cooperación',
				'CI':'Departamento de Computación y Tecnología de la Información',
				'CIB':'Departamento de Computación y Tecnología de la Información',
				'BC':'Departamento de Biología Celular',
				'BCB':'Departamento de Biología Celular',
				'BO':'Departamento de Biología de Organismos',
				'BOB':'Departamento de Biología de Organismos',
				'MT':'Departamento de Ciencia de los Materiales',
				'CMT':'Departamento de Ciencia de los Materiales',
				'GC':'Departamento de Ciencias de la Tierra',
				'CE':'Departamento de Ciencias Económicas y Admtvas.',
				'CEA':'Departamento de Ciencias Económicas y Admtvas.',
				'CS':'Departamento de Ciencias Sociales',
				'CSA':'Departamento de Ciencias Sociales',
				'CSX':'Departamento de Ciencias Sociales',
				'CSY':'Departamento de Ciencias Sociales',
				'CSZ':'Departamento de Ciencias Sociales',
				'EGS':'Departamento de Ciencias Sociales',
				'CC':'Departamento de Ciencias y Tec. del Comportamiento',
				'CCE':'Departamento de Ciencias y Tec. del Comportamiento',
				'CT':'Departamento de Conversión y Transporte de Energía',
				'CTE':'Departamento de Conversión y Transporte de Energía',
				'DA':'Departamento de Diseño Arquitectura y Artes Plásticas',
				'DAP':'Departamento de Diseño Arquitectura y Artes Plásticas',
				'DAA':'Departamento de Diseño Arquitectura y Artes Plásticas',
				'EC':'Departamento de Electrónica y Circuitos',
				'EYC':'Departamento de Electrónica y Circuitos',
				'EA':'Departamento de Estudios Ambientales',
				'EAD':'Departamento de Estudios Ambientales',
				'FF':'Departamento de Filosofía',
				'FL':'Departamento de Filosofía',
				'FS':'Departamento de Física',
				'FSI':'Departamento de Física',
				'FIS':'Departamento de Física',
				'FC':'Departamento de Formación General y Ciencias Básicas',
				'FCR':'Departamento de Formación General y Ciencias Básicas',
				'FCA':'Departamento de Formación General y Ciencias Básicas',
				'FCB':'Departamento de Formación General y Ciencias Básicas',
				'FCC':'Departamento de Formación General y Ciencias Básicas',
				'FCE':'Departamento de Formación General y Ciencias Básicas',
				'FCF':'Departamento de Formación General y Ciencias Básicas',
				'FCG':'Departamento de Formación General y Ciencias Básicas',
				'FCH':'Departamento de Formación General y Ciencias Básicas',
				'FCI':'Departamento de Formación General y Ciencias Básicas',
				'FCL':'Departamento de Formación General y Ciencias Básicas',
				'FCR':'Departamento de Formación General y Ciencias Básicas',
				'FCX':'Departamento de Formación General y Ciencias Básicas',
				'FCZ':'Departamento de Formación General y Ciencias Básicas',
				'FCW':'Departamento de Formación General y Ciencias Básicas',
				'ID':'Departamento de Idiomas',
				'IDM':'Departamento de Idiomas',
				'LL':'Departamento de Lengua y Literatura',
				'LLA':'Departamento de Lengua y Literatura',
				'LLB':'Departamento de Lengua y Literatura',
				'LLC':'Departamento de Lengua y Literatura',
				'LLE':'Departamento de Lengua y Literatura',
				'EGL':'Departamento de Lengua y Literatura',
				'MA':'Departamento de Matemáticas Puras y Aplicadas',
				'MAT':'Departamento de Matemáticas Puras y Aplicadas',
				'MC':'Departamento de Mecánica',
				'MEC':'Departamento de Mecánica',
				'PL':'Departamento de Planificación Urbana',
				'PLX':'Departamento de Planificación Urbana',
				'PLY':'Departamento de Planificación Urbana',
				'PS':'Departamento de Procesos y Sistemas',
				'PRS':'Departamento de Procesos y Sistemas',
				'QM':'Departamento de Química',
				'QIM':'Departamento de Química',
				'PB':'Departamento de Tecnol. de Proc. Biolog. y Bioquímicos',
				'TS':'Departamento de Tecnología de Servicios',
				'TSX':'Departamento de Tecnología de Servicios',
				'TI':'Departamento de Tecnología Industrial',
				'TF':'Departamento de Termodinámica y Fenómenos de Transf.',
				'TFT':'Departamento de Termodinámica y Fenómenos de Transf.',
				'FC':'Departamento Form. General y Ccias. Básicas',
				'PG':'PROYECTO DE GRADO',
				'TD':'TESIS DOCTORAL',
				'TEG':'TRABA ESPECIAL DE GRADO',
				'TG':'TRABAJO DE GRADO',
				'(USB)':'TRABAJO DE GRADO',
				}

def extraerCodigo(texto):
	codigo = re.search('[A-Z]{2}(\-| |­)?[0-9]{4}|[A-Z]{3}(\-| |­)?[0-9]{3}',texto)
	if (codigo!=None):
		return codigo.group(0)
	else:
		return "NULL"

def extraerDepartamento(texto):
    pre=extraerCodigo(texto)
    print(pre)

    if (pre!=None):
	    cod=re.search('[A-Z]*',pre).group(0)
	    if (departamentos.get(cod)!=None):
	    	return departamentos.get(cod)
	    else:
	    	return "NULL"
    else:
        return "NULL"
# PRUEBAS
#print(extraerCodigo('CI 3715'))
#print(extraerDepartamento('CI 3715'))
#print(extraerCodigo('CI-3715'))
#print(extraerDepartamento('CI-3715'))
#print(extraerCodigo('BO1125'))
#print(extraerDepartamento('BO1125'))
#print(extraerCodigo('ZZ125'))
#print(extraerDepartamento('ZZ125'))