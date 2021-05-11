from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Url

def index(req):
    return HttpResponse("<h3>Here is your first Django app page!</h3>")

def show(req, id):
    return HttpResponse(f'<h3>Your short url doesn\'t exist yet!</h3>')