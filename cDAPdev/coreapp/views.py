from django.shortcuts import render, HttpResponse, redirect
from models import Model_cdap
from forms import Model_cdap_form

# Create your views here.

def registerModel(request):
    if request.method == 'POST':
        