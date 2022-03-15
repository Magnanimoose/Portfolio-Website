from django.shortcuts import render
from typing import ChainMap
from django.http.response import HttpResponseNotModified
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string 
from django.http import Http404

# Create your views here.
def index(request):
    return  render(request, "homepage/index.html")

def about(request):
    return render(request, "homepage/about.html")