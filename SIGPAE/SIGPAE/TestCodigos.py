import extraercodigo

# Como no todos los programas tienen la estructura necesaria para hacer las pruebas
# las pruebas deseadas, se generaron strings que cumplan con los requisitos de las pruebas

stringvacio=""			# Código vacío
letra="A"				# Código de una sóla letra
numero="1"				# Código de sólo un número
codigocorto="A1"		# Código más corto de lo usual
siglas="CI"				# Código sin números, sólo siglas
codsindep="AA1111"		# Código sin departamento asignado
codcorrido="CI3715"		# Código corrido, es decir, sin separadores de ningún tipo
codseparado="ID 1211"	# Código separado por un espacio
codguion="CE-3419"		# Código separado por un guión
codlargo="AAAA111"		# Código más largo de lo normal
codlargonum="BO12345"	# Código con número más largo de lo normal
codlower="ma1111"		# Código con siglas en minúscula

class TestExtracciones(unittest.TestCasa):

	def testVacioCodigo:				# Prueba para la extracción del código
		cod=stringvacio					# Código Ficticio
		codext=extraerCodigo(cod)		# Código Extraído
		self.assertEqual(codext,NULL)

	def testVacioDepartamento:			# Prueba para la extracción del departamento
		cod=extraerCodigo(stringvacio)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)

	def testLetraCodigo:
		cod=letra
		codext=extraerCodigo(cod)
		self.assertEqual(codext,NULL)

	def testLetraDepartamento:
		cod=extraerCodigo(letra)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)

	def testNumeroCodigo:
		cod=numero
		codext=extraerCodigo(cod)
		self.assertEqual(codext,NULL)

	def testNumeroDepartamento:
		cod=extraerCodigo(numero)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)

	def testCodigoCortoCodigo:
		cod=codigocorto
		codext=extraerCodigo(cod)
		self.assertEqual(codext,NULL)

	def testCodigoCortoDepartamento:
		cod=extraerCodigo(codigocorto)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)

	def testSiglasCodigo:
		cod=siglas
		codext=extraerCodigo(cod)
		self.assertEqual(codext,NULL)

	def testSiglasDepartamento:
		cod=extraerCodigo(siglas)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)

	def testCodSinDepCodigo:
		cod=codsindep
		codext=extraerCodigo(cod)
		self.assertEqual(codext,codsindep)

	def testCodSinDepDepartamento:
		cod=extraerCodigo(codsindep)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)

	def testCodCorridoCodigo:
		cod=codcorrido
		codext=extraerCodigo(cod)
		self.assertEqual(codext,codcorrido)

	def testCodCorridoDepartamento:
		cod=extraerCodigo(codcorrido)
		depext=extraerDepartamento(cod)
		self.assertNotEqual(depext,NULL)	# OJO

	def testCodSeparadoCodigo:
		cod=codseparado
		codext=extraerCodigo(cod)
		self.assertEqual(codext,codseparado)

	def testCodSeparadoDepartamento:
		cod=extraerCodigo(codseparado)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)		# OJO

	def testCodGuionCodigo:
		cod=codguion
		codext=extraerCodigo(cod)
		self.assertEqual(codext,codguion)

	def testCodGuionDepartamento:
		cod=extraerCodigo(codguion)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)		# OJO

	def testCodLargoCodigo:
		cod=codlargo
		codext=extraerCodigo(cod)
		self.assertEqual(codext,NULL)		# OJO!!!

	def testCodLargoDepartamento:
		cod=extraerCodigo(codlargo)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)		# OJO!!!

	def testCodLargoNumCodigo:
		cod=codlargonum
		codext=extraerCodigo(cod)
		self.assertEqual(codext,NULL)		# OJO!!!

	def testCodLargoNumDepartamento:
		cod=extraerCodigo(codlargonum)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)		# OJO!!

	def testCodLowerCodigo:
		cod=codlower
		codext=extraerCodigo(cod)
		self.assertEqual(codext,NULL)

	def testCodLowerDepartamento:
		cod=extraerCodigo(codlower)
		depext=extraerDepartamento(cod)
		self.assertEqual(depext,NULL)

# Hay que estar pendientes para lo de los casos de prueba de códigos más largo de lo
# normal. Los está agarrando y podría generar problemas. Hay 2 soluciones:
# 1- Dejarlo así y ya
# 2- Editar la expresión regular de manera que ÚNICAMENTE agarre los casos que nos
# interesan. En tal caso, la expresión regular sería la siguiente:
# '[A-Z][A-Z](\-| )*[0-9][0-9][0-9][0-9]|[A-Z][A-Z][A-Z](\-| )*[0-9][0-9][0-9]'

# OJO: También hay peos con la cantidad de guiones y/o espacios en medio del código
# de una materia pero ahí sí estoy pelando bolas sobre cómo cambiar la expresión xD