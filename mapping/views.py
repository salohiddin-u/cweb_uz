from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *

import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def shorten(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        elements_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "A", "B", "C", "D"]
        elements = random.sample(elements_list, k=4)
        short_id = "".join(elements)

        while UrlMapping.objects.filter(short_id=short_id).exists():
            elements = random.sample(elements_list, k=4)
            short_id = "".join(elements)

        UrlMapping.objects.create(long_url=long_url, short_id=short_id)

        return redirect(f'/created/{short_id}/')

def created(request, short_id):
    base_url = f"{request.get_host()}/{short_id}"
    long_url = UrlMapping.objects.get(short_id=short_id).long_url
    context = {
                "base_url": base_url,
                "long_url": long_url,
            }
    return render(request, "success.html", context)

def url_redirect(request, short_id):
    url = get_object_or_404(UrlMapping, short_id=short_id)
    return redirect(url.long_url, permanent=True)