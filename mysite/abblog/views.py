from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def bday(request):

    #template = loader.get_template('index.html')
    return render(request,'abblog/index.html',{})