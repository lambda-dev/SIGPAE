from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.forms.formsets import formset_factory
from django.forms import inlineformset_factory
from readpdf import *
from datetime import *
import os
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'historia1/index.html')

def buscar(request):
    return render(request, 'historia1/buscar.html')

def buscar_t(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        docs = False
        if form.is_valid():
            codigo = form.cleaned_data['codigo'].upper()
            year = form.cleaned_data['year']
            trim = form.cleaned_data['trimestre']
            if year is not None:
                docs = Document.objects.all().filter(codigo=codigo,year=year,trimestre=trim)
            else:
                docs = Document.objects.all().filter(codigo=codigo)
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
                docs = Programa.objects.all().filter(codigo=codigo, fecha_vigtrim=trim, fecha_vigano=year)
            else:
                docs = Programa.objects.all().filter(codigo=codigo)
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

            doc.pdf_to_text = strng
            doc.save()
            document = Document.objects.get(name=str(request.FILES['document']))

            return redirect('mivista', document.id)
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

    form = SaveForm(request.POST or None, instance=doc)
    if form.is_valid():
        month = 1
        if form.cleaned_data['trimestre'] == 'EM':
            month = 1
        elif form.cleaned_data['trimestre'] == 'AB':
            month = 4
        elif form.cleaned_data['trimestre'] == 'SD':
            month = 9

        if form.cleaned_data['year'] is not None: 
            fecha = date(form.cleaned_data['year'], month, 1)

        temp = form.save(commit=False)
        temp.fecha = fecha
        temp.pdf_to_text = request.session['strng']
        temp.codigo = form.cleaned_data['codigo'].upper()
        temp.save()
        return redirect('model_form_upload')
    return render(request, 'historia1/editar.html', {'strng': strng, 'url': url, 'form_s': form})

def mivista(request, pk):
    ## TODO
    # GUARDAR STRNG SI LO MODIFICO !!
    doc = get_object_or_404(Document, pk=pk)
    url = doc.document.url
    strng = doc.pdf_to_text
    FormSet1 = formset_factory(AutForm)
    data1 = {'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
            'form-0-name':'',
            'form-0-apellido':'',
            }
    data2 = {'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
            'form-0-titulo':'',
            'form-0-editorial':'',
            'form-0-edicion':'',
            'form-0-name':'',
            'form-0-apellido':'',
            }

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
    form = SaveForm(request.POST or None, instance=doc)
    print(form_1.is_valid())
    print(form_2.is_valid())
    if form.is_valid() and form_1.is_valid() and form_2.is_valid():
        month = 1
        if form.cleaned_data['trimestre'] == 'EM':
            month = 1
        elif form.cleaned_data['trimestre'] == 'AB':
            month = 4
        elif form.cleaned_data['trimestre'] == 'SD':
            month = 9

        if form.cleaned_data['year'] is not None: 
            fecha = date(form.cleaned_data['year'], month, 1)
        else:
            fecha = date(2017,month,1)

        #temp = form.save(commit=False)  
        #temp.fecha = fecha
        #temp.pdf_to_text = request.session['strng']
        #temp.codigo = form.cleaned_data['codigo'].upper()
        #temp.save()
        print(form.is_valid()) 
        #form_1.save()
        print(request.POST.get('titulo',0))  
        print("HOLA___")

        return redirect('model_form_upload')
    #form_1.save()
    print("HOLA")
                
    return render(request, 'historia1/editar.html', {'strng': strng, 'url': url, 'form_s': form,'form_1': form_1,'form_2': form_2,'form_3': form_3,'form_4': form_4,'form_5': form_5,'form_6': form_6,'form_7': form_7,'form_8': form_8,'form_9': form_9,'form_10': form_10})



    # if request.method == 'POST':
    #     form = SaveForm(request.POST, instance=doc)
    #     if form.is_valid():
    #         month = 1
    #         if form.cleaned_data['trimestre'] == 'EM':
    #             month = 1
    #         elif form.cleaned_data['trimestre'] == 'AB':
    #             month = 4
    #         elif form.cleaned_data['trimestre'] == 'SD':
    #             month = 9
    #         fecha = date(form.cleaned_data['year'], month, 1)
    #         temp = form.save(commit=False)
    #         temp.fecha = fecha
    #         temp.pdf_to_text = request.session['strng']
    #         temp.codigo = form.cleaned_data['codigo'].upper()
    #         temp.save()
    #         return redirect('model_form_upload')
    #     else:
    #         strng = request.session['strng']
    #         form_s = SaveForm(instance = doc)
    #         return render(request,'historia1/editar.html', {'strng': strng, 'url': url, 'form_s': form})

    # else:
    #     strng = request.session['strng']
    #     form_s = SaveForm()
    #     return render(request,'historia1/editar.html', {'strng': strng, 'url': url, 'form_s': form_s})
    