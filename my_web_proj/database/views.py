import re
from django.shortcuts import render

# Create your views here.
def db_home(req):
    return render(req, 'main/plug.html')