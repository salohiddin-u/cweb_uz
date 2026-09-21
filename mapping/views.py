from django.shortcuts import render, redirect, get_object_or_404

from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def url_shortening(request):
    return render(request, 'success.html')

def url_redirect(request, short_id):
    url = get_object_or_404(UrlMapping, short_id=short_id)
    return redirect(url.long_url, permanent=True)