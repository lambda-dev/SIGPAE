from django.shortcuts import render, redirect
from .forms import DocumentForm, SaveForm
from .models import Document
from readpdf import *
import os
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return redirect(model_form_upload)

def model_form_upload(request):
    print(request.session.items())
    error = ""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

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
            strng = leer('documents/'+str(request.FILES['document']))
            request.session['strng'] = strng['texto']
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
            form.save()
            form1 = DocumentForm()
            error = "GUARDADO"
            return redirect('model_form_upload')

    else:
        strng = request.session['strng']
        url = request.session['url']
        form_s = SaveForm(instance = document)
        return render(request,'historia1/editar.html', {'strng': strng, 'url': url, 'form_s': form_s})
