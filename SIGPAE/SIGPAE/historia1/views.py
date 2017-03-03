from django.shortcuts import render, redirect
from .forms import DocumentForm, SaveForm, SearchForm
from .models import Document
from readpdf import *
from datetime import *
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

            return redirect('editar_t')
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
