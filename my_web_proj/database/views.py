import re
from django.shortcuts import render

# Create your views here.


'''db start page'''
def db_start(req):
    return render(req,'database/db.html')