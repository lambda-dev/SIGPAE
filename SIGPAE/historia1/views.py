from django.shortcuts import render
from .forms import DocumentForm
from readpdf import *
# Create your views here.
from django.http import HttpResponse

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            strng =leer("LLA-111.pdf")
            return redirect('home')
    else:
        form = DocumentForm()
        strng =leer("LLA-111.pdf")
    return render(request,'historia1/model_form_upload.html', {
        'form': form,
        'strng' : strng
    })
