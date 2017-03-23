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

import os
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'historia1/index.html')

def buscar(request):
    return render(request, 'historia1/buscar.html')

def buscar_s(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['year']
            trim = form.cleaned_data['trimestre']
            if year is not None:
                docs = Document.objects.all().filter(codigo=codigo,year=year,trimestre=trim,guardar="PASA").order_by('-year')
            else:
                docs = Document.objects.all().filter(codigo=codigo,guardar="PASA").order_by('-year')
        return render(request, 'historia1/buscar_s.html', {'form': form, 'query': docs})
    else:
        form = SearchForm()
        return render(request, 'historia1/buscar_s.html', {'form': form})

def view_s(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if doc.guardar == 'TRAN':
        return redirect('index')

    form = ViewPASAForm(request.POST or None, instance=doc)
    return render(request, 'historia1/view_s.html', {'form':form})

def buscar_t(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['year']
            trim = form.cleaned_data['trimestre']
            if year is not None:
                docs = Document.objects.all().filter(codigo=codigo,year=year,trimestre=trim,guardar="TRAN").order_by('-year')
            else:
                docs = Document.objects.all().filter(codigo=codigo,guardar="TRAN").order_by('-year')
        return render(request, 'historia1/buscar_t.html', {'form': form, 'query': docs})
    else:
        form = SearchForm()
        return render(request, 'historia1/buscar_t.html', {'form': form})

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

def view_p(request, pk):
    prog = get_object_or_404(Programa, pk=pk)
    form = ViewProgForm(request.POST or None, instance=prog)
    return render(request, 'historia1/view_p.html', {'form':form})

def editar_t(request, pk):
    ## TODO
    # GUARDAR STRNG SI LO MODIFICO !!
    doc = get_object_or_404(Document, pk=pk)
    url = doc.document.url
    strng = doc.pdf_to_text

    codigo = extraerCodigo(strng)
    departamento = extraerDepartamento(codigo)

    campos = ['asignatura','codigo','creditos','year', 'trimestre','fecha',
            'departamento','requisitos','justificacion','objetivos','contenidos',
            'metodologias','evaluacion','bibliografias','horas_teoria','horas_lab',
            'horas_practica','guardar']

    if doc.guardar == 'PASA':
        return redirect('index')

    FormSet1 = formset_factory(AutForm)
    form_1=RefForm(request.POST or None)
    #LibroFormset = inlineformset_factory(Referencia,Autores,fields=['name','apellido',])
    form_2=FormSet1(request.POST or None)
    form_3=RefForm(request.POST or None)
    form_4=FormSet1(request.POST or None)
    form_5=RefForm(request.POST or None)
    form_6=FormSet1(request.POST or None)
    form_7=RefForm(request.POST or None)
    form_8=FormSet1(request.POST or None)
    form_9=RefForm(request.POST or None)
    form_10=FormSet1(request.POST or None)

    FormSet = formset_factory(ExtraFields, formset=BaseLinkFormSet)
    requeridos = ['requisitos','objetivos','metodologias','evaluacion','justificacion']

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
    if form.is_valid() and form_.is_valid() and form_1.is_valid() and form_2.is_valid():
        temp = form.save(commit=False)
        if form.cleaned_data['fecha'] is not None:
            month = 1
            if form.cleaned_data['trimestre'] == 'EM':
                month = 1
            elif form.cleaned_data['trimestre'] == 'AB':
                month = 4
            elif form.cleaned_data['trimestre'] == 'SD':
                month = 9

            if form.cleaned_data['year'] is not None: 
                fecha = date(form.cleaned_data['year'], month, 1)
                temp.fecha = fecha

        for d in data:
            d.delete()
            
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

        # PARA PASA => VERIFICAR QUE CAMPOS OBLI NO VACIOS, OTRAS RESTRICCIONES
        if form.cleaned_data['guardar'] == 'PASA':
            return redirect('form_pasa', pk)
        else:
            return redirect('/editar/'+pk+'')

    return render(request, 'historia1/editar.html', {'departamento': departamento, 'codigo': codigo,'strng': strng, 'url': url, 'form_s': form, 
                                                    'requeridos':requeridos,'form_':form_,'act':y,'form_1': form_1,'form_2': form_2,'form_3': form_3,'form_4': form_4,'form_5': form_5,'form_6': form_6,'form_7': form_7,'form_8': form_8,'form_9': form_9,'form_10': form_10})

def form_pasa(request, pk):
    if request.method == 'POST':
        doc = get_object_or_404(Document, pk=pk)
        form = PASAForm(request.POST or None, instance=doc)
        
        if form.is_valid():
            form.save()
            return redirect('/?msg=pasa_saved')
            
        return render(request, 'historia1/pasa.html', {'form':form, 'pk':pk})
    return redirect('/?msg=error')
