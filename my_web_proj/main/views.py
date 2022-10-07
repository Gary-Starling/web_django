from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''welcome page'''
def welcome(req):
    return render(req, 'main/index.html')

'''contacts page'''
def author(req):
    return render(req, 'main/author.html')

    
    
    