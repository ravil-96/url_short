from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GenerateUrlForm
from .models import Url

def index(req):
    return render(req, 'app/index.html')

def show(req, id):
    return HttpResponse(f'<h3>Your short url doesn\'t exist yet!</h3>')