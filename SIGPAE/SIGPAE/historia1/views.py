from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import Document
from readpdf import *
from datetime import *
from django import forms
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
import os
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    #return redirect(model_form_upload)
    return render(request, 'historia1/index.html')

def buscar(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            docs = Document.objects.all().filter(codigo=form.cleaned_data['codigo'])
        return render(request, 'historia1/buscar.html', {'form': form, 'query': docs})
    else:
        form = SearchForm()
        return render(request, 'historia1/buscar.html', {'form': form})

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
                error = "UN ERROR HA OCURRIDO, ARCHIVO EN FORMATO ERRONEO"
                return render(request,'historia1/model_form_upload.html',
                {
                'form' : form1,
                'error': error
                })
            try:
                search = Document.objects.get(name=doc.name)
                form1 = DocumentForm()
                error = "ERROR. YA EXISTE UN ARCHIVO CON ESE NOMBRE"
                return render(request,'historia1/model_form_upload.html',
                {
                'form' : form1,
                'error': error
                })
            except Document.DoesNotExist:
                pass

            doc.save()
            if scan:
                strng = leerImg('documents/'+str(request.FILES['document']))
            else:
                strng = leer('documents/'+str(request.FILES['document']))
            request.session['strng'] = strng
            url = doc.document.url
            request.session['url'] = url
            request.session['name'] = str(request.FILES['document'])
            return redirect('nueva_vista')
    else:
        form = DocumentForm()
    return render(request,'historia1/model_form_upload.html', {
    'form' : form, 'error': error
    })


def editar_t(request):
    name = request.session['name']
    document = Document.objects.get(name=name)
    if request.method == 'POST':
        form = SaveForm(request.POST, instance=document)
        if form.is_valid():
            month = 1
            if form.cleaned_data['trimestre'] == 'EM':
                month = 1
            elif form.cleaned_data['trimestre'] == 'AB':
                month = 4
            elif form.cleaned_data['trimestre'] == 'SD':
                month = 9
            fecha = date(form.cleaned_data['year'], month, 1)
            temp = form.save(commit=False)
            temp.fecha = fecha
            temp.save()
            return redirect('model_form_upload')
        else:
            strng = request.session['strng']
            url = request.session['url']
            form_s = SaveForm(instance = document)
            return render(request,'historia1/editar.html', {'strng': strng, 'url': url, 'form_s': form})

    else:
        strng = request.session['strng']
        url = request.session['url']
        form_s = SaveForm(instance = document)
        return render(request,'historia1/editar.html', {'strng': strng, 'url': url, 'form_s': form_s})

def nueva_vista(request):


    name = request.session['name']
    document = Document.objects.get(name=name)
    campos = ['name','description','asignatura','codigo','creditos','requisitos','objetivos','contenidos',
    'metodologias','evaluacion','bibliografias','horas_teoria','fecha','horas_lab',
    'horas_practica','year','justificacion','trimestre','departamento']

    FormSet = formset_factory(ExtraFields, formset=BaseLinkFormSet)
    # fields = CamposExtra.objects.find(document = document)
    # data = [{'nombre':l.nombre, 'value': l.value, 'document':l.document} for l in fields]

    requeridos = ['requisitos','objetivos','metodologias','evaluacion','justificacion']

    y = {}
    for x in campos:
        y_x=document.__getattribute__(x)
        if y_x is not None and y_x != '':
            y[x] = y_x

    if request.method == 'POST':

        form_ = FormSet(request.POST)
        form = SaveForm(request.POST, instance=document)
        if form.is_valid() and form_.is_valid():
            month = 1
            if form.cleaned_data['trimestre'] == 'EM':
                month = 1
            elif form.cleaned_data['trimestre'] == 'AB':
                month = 4
            elif form.cleaned_data['trimestre'] == 'SD':
                month = 9
            fecha = date(form.cleaned_data['year'], month, 1)
            temp = form.save(commit=False)
            temp.fecha = fecha

            print('a')

            #new = []
            for l in form_:
                print('guradadsadas')
                nombre = l.cleaned_data.get('nombre')
                value = l.cleaned_data.get('value')
                c = CamposExtra(nombre=nombre,value=value)
                c.save()
                c.document.add(document)
                c.save()
                #new.append(c)
            #
            # try:
            #     with transaction.atomic():
            #         CamposExtra.objects.bulk_create(new)
            #         #messages.success(request, 'You have updated your profile.')
            #
            # except IntegrityError: #If the transaction failed
            #     messages.error(request, 'Error al guardar')


            return redirect('model_form_upload')
        else:
            strng = request.session['strng']
            url = request.session['url']
            form_s = SaveForm(instance = document)

            print('b')
            return render(request,'historia1/editar_.html', {'strng': strng, 'url': url, 'form_s': form,
            'requeridos':requeridos,'form_':form_,'act':y})

    else:
        strng = request.session['strng']
        url = request.session['url']
        form_s = SaveForm(instance = document)
        data = CamposExtra.objects.filter(document=document)
        initial_data = [{'nombre':d.nombre,'value':d.value} for d in data]
        form_ = FormSet(initial = initial_data)

        #print (y)

        print('c')
        return render(request,'historia1/editar_.html', {'strng': strng, 'url': url,
         'form_s': form_s,'requeridos':requeridos,'form_':form_,'act':y})
