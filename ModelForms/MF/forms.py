from django import forms
from MF.models import Movie
#from MF.models import Student

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

'''
class StudentForm(forms.ModelForm):
    #fields with Validations...
    class Meta:
        model=Student
        fields='__all__'
'''