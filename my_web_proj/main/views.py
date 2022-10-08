from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''home page'''
def home(req):
    return render(req, 'main/home.html')

'''contacts page'''
def contacts(req):
    return render(req, 'main/contacts.html')

'''about page'''
def about(req):
    return render(req, 'main/about.html')

'''contacts page'''
def details(req):
    return render(req, 'main/details.html')

    
    
    