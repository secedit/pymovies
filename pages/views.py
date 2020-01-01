from django.shortcuts import render,redirect
from django.http import HttpResponse


#Comment App ve Message App ile ilgili importlar
import datetime
from django.contrib import messages
from comments import models as commentModel
from movies.models import Movie
from random import sample
from django.db.models import Q

from movies.views import get_slider, get_on_imdb

# Create your views here.

def index(request):
    context = {}
    movies1 = get_movie_queryset('')
    movies = Movie.objects.all()
    context['movies1'] = movies1
    context['movies'] = movies

    get_slider(context)
    get_on_imdb(context)

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
    
def contact(request):
    return render(request, 'pages/contact.html')

def sendMessage(request):

    if request.user.is_authenticated:
         email = request.user.email 
    else:
         email = request.POST['email']
    #eger kullanici giris yaptiysa mevcut kullanici emailini al, degilse post edilen emaili al

    name = request.POST['name']
    surname = request.POST['surname']
    message = request.POST['message']
    date = datetime.datetime.now().date()

    newMessage = commentModel.Message(email = email, name = name, surname = surname, message = message, created_date = date )
    newMessage.save()
    #message tablosuna yeni veriler kaydettik

    messages.success(request, 'Mesajiniz basariyla gonderildi.')


    return redirect('contact')

def get_movie_queryset(query=None):
    queryset = []
    movies = Movie.objects.filter(Q(turu__contains=query)).distinct()
    for movie in movies:
        queryset.append(movie)
    queryset_new = sample(queryset, 16)
    return list(set(queryset_new))