from django.shortcuts import render
import pandas as pd
import json
from apps.core.models import Department
from django.db import IntegrityError
# Create your views here.

def index(request):
    df = pd.read_pickle("Input_Dataframe.pckl")
    depart = list(df.Department.unique())
    for d in depart:
        try:
            Department.objects.create(name = d)
        except IntegrityError:
            pass
    query_results = Department.objects.all();

    # Creating a dictionary to pass as an argument
    context = { 'query_results' : query_results }
    return render(request, template_name='index.html', context=context)

def dash_desing(request,name):
    query_results = Department.objects.all();

    # Creating a dictionary to pass as an argument
    context = { 'query_results' : query_results }
    return render(request, template_name='design.html', context=context)

def dash_engineering(request):
    return render(request, template_name='engineering.html', context=None)

def dash_accounting(request):
    return render(request, template_name='accounting.html', context=None)