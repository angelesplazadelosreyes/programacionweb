from urllib import request
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def index(request):

    return render(request,"index.html")