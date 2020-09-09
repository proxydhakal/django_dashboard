import json
import pandas as pd
from django.shortcuts import render
from django.db import IntegrityError
from apps.core.models import Department


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
    context = { 'query_results' : query_results }
    return render(request, template_name='index.html', context=context)

def dashboardView(request,name):
    
    query_results = Department.objects.all();
    df = pd.read_pickle("Input_Dataframe.pckl")
    depart = list(df.Department.unique())
    list_depart1 = df.loc[df['Department'] == depart[0]]
    list_depart2 = df.loc[df['Department'] == depart[1]]
    new_df1 = list_depart1.loc[df['Section'] == 'Bottom']
    new_df2 = list_depart2.loc[df['Item'] == 'Jobs']
    index1 = int(new_df1[new_df1['Section']=='Bottom'].index.values)
    index2 = int(new_df2[new_df2['Item']=='Jobs'].index.values)
    table1=list_depart1['Text'][index1].to_html(index=False,justify='left')
    table2=list_depart2['Text'][index2].to_html(index=False,justify='left')
    context = { 'query_results' : query_results, 'data': table1,'data1':table2}
    if name == 'Design':
        template_name='design.html'
    elif name == 'Engineering':
        template_name='engineering.html'
    else:
        template_name='accounting.html'

    return render(request, template_name, context=context)
