from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from . import models
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def contact(request):
    return render(request, 'pages/contact.html')


def about(request):
    return render(request, 'pages/about.html')

def tag(request, nom):
    data ={
        'titre':nom
    }
    return render(request, 'pages/tag.html', data)

def categorie(request, nom):
    data ={
        'titre':nom
    }
    return render(request, 'pages/categorie.html', data)

def detail(request, titre):
    data ={
        'titre':titre
    }
    return render(request, 'pages/single.html', data)