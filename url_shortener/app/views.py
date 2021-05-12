from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GenerateUrlForm
from .models import Url
import random
import string

def index(req):
    if req.method == 'POST':
        form = GenerateUrlForm(req.POST)
        if form.is_valid():
            url = form.save(commit=False)
            if url.original[:8] == 'https://' or url.original[:7] == 'http://':
                pass
            elif url.original[:4] == 'www.':
                url.original = 'https://' + url.original
            else:
                url.original = 'https://www.' + url.original
            if len(Url.objects.filter(original = url.original)) > 0:
                result = {'result': Url.objects.get(original=url.original).short_url}
                return render (req, 'app/newurl.html', result)
            possible_symbols = string.ascii_lowercase + '1234567890'
            random_string = ''.join(random.choice(possible_symbols) for i in range(5))
            while len(Url.objects.filter(short_url=random_string)) > 0:
                random_string = ''.join(random.choice(possible_symbols) for i in range(5))
            url.short_url = random_string
            url.save()
            result = {'result': random_string}
            return render (req, 'app/newurl.html', result)

    else :
        data = {'form': GenerateUrlForm}
        return render(req, 'app/index.html', data)

def show(req, id):
    try:
        url = Url.objects.get(short_url=id)
        return redirect(url.original)
    except Url.DoesNotExist:
        return redirect('app-index')