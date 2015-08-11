from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import URLInfo
from .forms import URLForm
import re
import requests
import html

# Create your views here.
def url_list(request):
    urls = URLInfo.objects.all()
    return render(request, 'url_list.html', {'urls' : urls})

def url_detail(request, pk):
    url = get_object_or_404(URLInfo, pk=pk)
    if url.status_code[0] == '2':
        ok = True
    else:
        ok = False
    return render(request, 'url_detail.html', {'url' : url, 'ok' : ok})

def url_new(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            req = requests.get(form.cleaned_data['short_url'])
            url.expanded_url = req.url
            url.status_code = req.status_code
            try:
                url.page_title = html.unescape(re.compile('<title>(.*)</title>').search(req.text).group(1))
            except AttributeError:
                url.page_title = 'No title available'
            url.save()
            return redirect('app.views.url_detail', pk=url.pk)
    else:
        form = URLForm()
    return render(request, 'url_new.html', {'form' : form})

def url_remove(request, pk):
    url = get_object_or_404(URLInfo, pk=pk)
    url.delete()
    return redirect('app.views.url_list')
