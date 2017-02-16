from django.shortcuts import render
from .forms import DocumentForm
from readpdf import *
import os
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def after_upload(request):
    return render(request,'historia1/after_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            filename, file_extension = os.path.splitext('documents/'+str(request.FILES['document']))
            if file_extension != ".pdf":
                form1 = DocumentForm()
                return render(request,'historia1/model_form_error.html',
                {
                'form' : form1
                })

            strng =leer('documents/'+str(request.FILES['document']))
            return render(request,'historia1/editar.html',
            {
            'strng' : strng
            })
    else:
        form = DocumentForm()
    return render(request,'historia1/model_form_upload.html', {
    'form' : form
    })

def editar(request):
    return render(request,'historia1/editar.html')
