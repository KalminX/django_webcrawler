from .forms import InputForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
from .models import Mail
from .utils import generate_words


def crawl_result_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            words = generate_words(url)
            context = {'url': url, 'words': words}
            return render(request, 'wordcounter/send.html', context)
        else:
            form = InputForm()

    context = {'form': form}
    return render(request, 'wordcounter/home.html', context)

def crawl_view(request):
    form = InputForm()
    context = {'form': form}
    return render(request, 'wordcounter/home.html', context)
