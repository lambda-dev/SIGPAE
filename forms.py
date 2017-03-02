from django import forms
from .models import Document
from .models import Student

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('year_in_school', )
