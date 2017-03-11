import os
try:
    from pdfminer.pdfparser import PDFParser, PDFDocument
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import PDFPageAggregator
    from pdfminer.layout import LAParams, LTTextBox, LTTextLine

# Instala la libreria pdfminer3k en caso de no existir
except ImportError:
    print('No existe la libreria, presione enter para instalarla')
    input()
    try:
        import pip
        pip.main(['install','pdfminer3k'])
    except ImportError:
        print('No se encontro la libreria pip')

def leer(name):
    fp = open(name, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    txt = ''
    # Process each page contained in the document.
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                txt += lt_obj.get_text()
            txt += '\n'
    return txt

def leerImg(name):
    os.system('ocrmypdf -l spa+eng --rotate-pages --force-ocr ' + name + ' ' + 'output.pdf')
    try:
        w = leer('output.pdf')
        os.remove('output.pdf')
    except FileNotFoundError:
        w = leer(name)

    return w
