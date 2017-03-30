# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.forms.formsets import formset_factory
from django.forms import inlineformset_factory
from readpdf import *
from datetime import *
from django.contrib import messages
from django import forms
from django.db import IntegrityError, transaction
from extraercodigo import  * 
from itertools import chain

import os
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

# Index del sistema
def index(request):
    return render(request, 'historia1/index.html')

# VIEW: Reportes globales
# Hace queries a la base de datos segun el tipo para mostrar el reporte
def r_global(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            dep = form.cleaned_data['departamento']
            if form.cleaned_data['tipo'] == 'PP':
                query = Programa.objects.filter(departamento=dep).order_by('codigo', 'fecha_vigano')
            elif form.cleaned_data['tipo'] == 'TT':
                query = Document.objects.filter(departamento=dep).order_by('codigo', 'fecha_vigano')
            elif form.cleaned_data['tipo'] == 'ALL':
                query1 = Document.objects.filter(departamento=dep).order_by('codigo', 'fecha_vigano')
                query2 = Programa.objects.filter(departamento=dep).order_by('codigo', 'fecha_vigano')
                query = sorted(chain(query1, query2),
                        key=lambda row: row.codigo)
            else:
                query = False
            return render(request, 'historia1/global.html', {'form':form, 'query':query})
    else:
        form = ReportForm()
    return render(request, 'historia1/global.html', {'form': form})    

# VIEW: Buscar Por Aprobar
# Busca en la base de datos los documentos guardados Por Aprobar y los muestra
def buscar_s(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['fecha_vigano']
            trim = form.cleaned_data['fecha_vigtrim']
            if year is not None:
                docs = Document.objects.all().filter(codigo=codigo,fecha_vigano=year,fecha_vigtrim=trim,guardar="PASA").order_by('-fecha_vigano')
            else:
                docs = Document.objects.all().filter(codigo=codigo,guardar="PASA").order_by('-fecha_vigano')
        return render(request, 'historia1/buscar_s.html', {'form': form, 'query': docs})
    else:
        form = SearchForm()
        return render(request, 'historia1/buscar_s.html', {'form': form})

# VIEW: Ver Por Aprobar
# Muestra los campos del documento Por Aprobar, no deja editarlos
def view_s(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if doc.guardar == 'TRAN':
        return redirect('index')

    form = ViewPASAForm(request.POST or None, instance=doc)
    return render(request, 'historia1/view_s.html', {'form':form})

# VIEW: Buscar Transcripciones
# Busca en la base de datos los documentos guardados de tipo Transcripcion y los muestra
def buscar_t(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['fecha_vigano']
            trim = form.cleaned_data['fecha_vigtrim']
            if year is not None:
                docs = Document.objects.all().filter(codigo=codigo,fecha_vigano=year,fecha_vigtrim=trim,guardar="TRAN").order_by('-fecha_vigano')
            else:
                docs = Document.objects.all().filter(codigo=codigo,guardar="TRAN").order_by('-fecha_vigano')
        return render(request, 'historia1/buscar_t.html', {'form': form, 'query': docs})
    else:
        form = SearchForm()
        return render(request, 'historia1/buscar_t.html', {'form': form})

# VIEW: Buscar Programas
# Busca en la base de datos los documentos guardados de tipo Programa y los muestra
def buscar_p(request):
    if request.method == 'POST':
        form = SearchFormProg(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['fecha_vigano']
            trim = form.cleaned_data['fecha_vigtrim']
            if year is not None:
                docs = Programa.objects.all().filter(codigo=codigo, fecha_vigtrim=trim, fecha_vigano=year).order_by('-fecha_vigano')
            else:
                docs = Programa.objects.all().filter(codigo=codigo).order_by('-fecha_vigano')
        return render(request, 'historia1/buscar_p.html', {'form': form, 'query': docs})
    else:
        form = SearchFormProg()
        return render(request, 'historia1/buscar_p.html', {'form': form})

# VIEW: Subir PDF
# Formulario para subir los archivos PDF al sistema
def model_form_upload(request):
    error = ""
    scan=False
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if request.POST.get('scanned') == 'on':
            scan = True

        if form.is_valid():
            doc = form.save(commit = False)
            doc.name = request.FILES['document']
            filename, file_extension = os.path.splitext('documents/'+str(request.FILES['document']))
            if file_extension != ".pdf":
                form1 = DocumentForm()
                error = "Error: El archivo debe tener formato .pdf"
                return render(request,'historia1/model_form_upload.html',
                {
                'form' : form1,
                'error': error
                })

            doc.save()
            if scan:
                strng = leerImg('documents/'+str(request.FILES['document']))
            else:
                strng = leer('documents/'+str(request.FILES['document']))

            doc.pdf_to_text = strng
            doc.save()

            return redirect('editar_t', doc.id)
    else:        
        form = DocumentForm()

    return render(request,'historia1/model_form_upload.html', {
    'form' : form, 'error': error
    })

# VIEW: Mostrar Programa
# Muestra un documento de tipo Programa, con sus campos no editables
def view_p(request, pk):
    prog = get_object_or_404(Programa, pk=pk)
    form = ViewProgForm(request.POST or None, instance=prog)
    return render(request, 'historia1/view_p.html', {'form':form})

# VIEW: Editar
# Muestra el formulario responsable de editar las transcripciones, junto al manejo de campos extra
def editar_t(request, pk):
    ## TODO
    # GUARDAR STRNG SI LO MODIFICO !!
    doc = get_object_or_404(Document, pk=pk)
    url = doc.document.url
    strng = doc.pdf_to_text

    codigo = extraerCodigo(strng)
    departamento = extraerDepartamento(codigo)

    campos = ['asignatura','codigo','creditos','fecha_vigano', 'fecha_vigtrim','fecha',
            'departamento','requisitos','justificacion','objetivos','contenidos',
            'metodologias','evaluacion','horas_teoria','horas_lab',
            'horas_practica','guardar']

    if doc.guardar == 'PASA':
        return redirect('index')


    FormSet = formset_factory(ExtraFields, formset=BaseLinkFormSet)
    requeridos = ['justificacion']

    y = {}
    for x in campos:
        y_x=doc.__getattribute__(x)
        if y_x is not None and y_x != '':
            y[x] = y_x


    data = CamposExtra.objects.filter(document=doc)
    initial_data = [{'nombre':d.nombre,'value':d.value} for d in data]

    if request.method == 'POST':
        form_ = FormSet(request.POST)
    else:
        form_ = FormSet(initial = initial_data)

    form = SaveForm(request.POST or None, instance=doc)
    if form.is_valid() and form_.is_valid():
        temp = form.save(commit=False)

        for d in data:
            d.delete()
            
        for l in form_:
            nombre = l.cleaned_data.get('nombre')
            value = l.cleaned_data.get('value')
            try:
                c = CamposExtra(nombre=nombre,value=value)
                c.save()
                c.document.add(doc)
                c.save()
            except:
                pass

        temp.codigo = form.cleaned_data['codigo'].upper()
        temp.pdf_to_text = strng
        temp.save()
        # PARA PASA => VERIFICAR QUE CAMPOS OBLI NO VACIOS, OTRAS RESTRICCIONES
        if form.cleaned_data['guardar'] == 'PASA':
            return redirect('form_pasa', pk)
        else:
            return redirect('/editar/'+pk+'')

    return render(request, 'historia1/editar.html', {'departamento': departamento, 'codigo': codigo,'strng': strng, 'url': url, 'form_s': form, 
                                                    'requeridos':requeridos,'form_':form_,'act':y, 'pk': pk})

# VIEW: Formulario Por Aprobar
# Le pide al usuario los datos a guardar cuando es un documento Por Aprobar
def form_pasa(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    form = PASAForm(request.POST or None, instance=doc)
        
    if form.is_valid():
        form.save()
        return redirect('/?msg=pasa_saved')
            
    return render(request, 'historia1/pasa.html', {'form':form, 'pk':pk})

# VIEW: Referencias
# Muestra la pantalla donde se maneja el agregar las fuentes de información
def referencias(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':

        ### GUARDAR ####
        url = doc.document.url
        strng = doc.pdf_to_text
        FormSet = formset_factory(ExtraFields, formset=BaseLinkFormSet)
        form_ = FormSet(request.POST)

        form = SaveForm(request.POST or None, instance=doc)
        if form.is_valid() and form_.is_valid():
            temp = form.save(commit=False)
                
            for l in form_:
                nombre = l.cleaned_data.get('nombre')
                value = l.cleaned_data.get('value')
                c = CamposExtra(nombre=nombre,value=value)
                c.save()
                c.document.add(doc)
                c.save()

            temp.codigo = form.cleaned_data['codigo'].upper()
            temp.pdf_to_text = strng
            temp.save()
        ######## GUARDAR #####################

            query = Referencia.objects.filter(document=doc)
        return render(request, 'historia1/referencias.html', {'query':query, 'pkD':pk})
    else:
        query = Referencia.objects.filter(document=doc)
        return render(request, 'historia1/referencias.html', {'query':query, 'pkD':pk})

# VIEW: Añadir libro nuevo
# Añade un libro nuevo a las fuentes de información
def add_ref(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = RefForm(request.POST)
        if form.is_valid():
            query1 = Document.objects.filter(pk=pk)
            form.cleaned_data['document'] = query1
            form.save()
            return redirect('/editar/referencias/'+pk+'')
    else:
        form = RefForm()
    return render(request, 'historia1/add_ref.html', {'pk':pk, 'form':form, 'url': doc.document.url})

# VIEW: Ver datos extra de la Fuente
# Permite ver todos los autores y todos los datos extra de la fuente y permite elegir cual añadir
def add_extra(request, pkD, pkR):
    query = Autores.objects.filter(referencia=pkR)
    query2 = DatosReferencia.objects.filter(referencia=pkR)
    return render(request, 'historia1/add_extra.html', {'pkD':pkD, 'pkR':pkR, 'query':query,'query2':query2})

# VIEW: Añadir Autor
# Permite añadir autores nuevos a la fuente de información
def add_autores(request, pkD, pkR):
    doc = get_object_or_404(Document, pk=pkD)
    form = AutForm()
    if request.method == 'POST':
        form = AutForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            ref = get_object_or_404(Referencia, pk=pkR)
            temp.referencia = ref
            temp.save()

        return redirect('/add/referencias/extra/'+pkD+'/'+pkR)
    return render(request, 'historia1/add_autor.html', {'form':form, 'url': doc.document.url})

# VIEW: Añadir datos de la Fuente
# Añade datos extra a la fuente de información, como editorial, año, etc
def add_extras(request, pkD, pkR):
    doc = get_object_or_404(Document, pk=pkD)
    form = FormDatosRef()
    if request.method == 'POST':
        form = FormDatosRef(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            ref = get_object_or_404(Referencia, pk=pkR)
            temp.referencia = ref
            temp.save()

        return redirect('/add/referencias/extra/'+pkD+'/'+pkR)
    return render(request, 'historia1/add_notas.html', {'form':form, 'url': doc.document.url})