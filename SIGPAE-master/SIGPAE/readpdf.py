try:
	from PyPDF2 import PdfFileReader
except ImportError: # Instala la libreria PyPDF2 en caso de no existir
	print('No existe la libreria, presione enter para instalarla')
	#raw_input()
	import pip
	pip.main(['install','PyPDF2'])

#archivo=raw_input("Introduzca el nombre del PDF a leer\n")
def leer(archivo):
	input = PdfFileReader(open(archivo, "rb"))

	#print("Leyendo "+(input.getDocumentInfo().title)+".pdf")
	texto = ""
	for i in range(0,input.getNumPages()):
		texto += input.getPage(i).extractText()
		#print("\n")

	return dict(numP=input.getNumPages(),
				title=input.getDocumentInfo().title,
				input=input,
				texto = texto)
