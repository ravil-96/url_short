from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GenerateUrlForm
from .models import Url

def index(req):
    if req.method == 'POST':
        form = GenerateUrlForm(req.POST)
        if form.is_valid() :
            url = form.save()
            shortUrl = "hello.com"
            result = {'result': shortUrl}
            return render (req, 'app/newurl.html', result)

    else :
        data = {'form': GenerateUrlForm}
        return render(req, 'app/index.html', data)

def show(req, id):
    return HttpResponse(f'<h3>Your short url doesn\'t exist yet!</h3>')