from django.shortcuts import render
from . import forms
from MF.forms import MovieForm
from MF.models import Movie

# Create your views here.
def index_v(request):
    return render(request,'mf/index.html')

def add_movie(request):
    form = MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_v(request)
    return render(request,'mf/addmovie.html',{'form':form})

def list_movie(request):
    movie_list = Movie.objects.all()
    return render(request,'mf/listmovie.html',{'movie_list':movie_list})




'''
def Student_view(request):
    #if request.method=='GET':
    form=forms.StudentForm
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'mf/stu.html',{'form':form})
'''
