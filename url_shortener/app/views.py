from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GenerateUrlForm
from .models import Url
import random
import string

def index(req):
    if req.method == 'POST':
        form = GenerateUrlForm(req.POST)
        if form.is_valid() :
            url = form.save()
            random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            url.short_url = random_string
            url.save()
            result = {'result': random_string}
            return render (req, 'app/newurl.html', result)

    else :
        data = {'form': GenerateUrlForm}
        return render(req, 'app/index.html', data)

def show(req, id):
    print(id, type(id))
    url = Url.objects.get(short_url=id)
    print(url)
    return HttpResponse(f'<h3>Url: {url.original}</h3>')