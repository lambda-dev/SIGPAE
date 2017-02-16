from django.shortcuts import render
from .forms import DocumentForm
from readpdf import *
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
            strng =leer('documents/'+str(request.FILES['document']))
            return render(request,'historia1/after_upload.html', {
                'strng' : strng})
    else:
        form = DocumentForm()
        #strng =leer(str(request.FILES['document']))
    return render(request,'historia1/model_form_upload.html', {
        'form' : form
    })
