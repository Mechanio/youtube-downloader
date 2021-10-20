from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
import pytube
import os


def index(request):
    searchform = SearchForm()
    context = {
        'searchform': searchform
    }
    if request.method == 'POST':
        form = request.POST['search_field']
        p = pytube.Playlist(form)
        context['videos'] = p.videos
        context['urls'] = p.video_urls

    return render(request, 'main/index.html', context)

# https://www.youtube.com/playlist?list=PLONPqVvA6oEV5xAUUB1OwB-TP9swKXGPT
def about(request):
    return render(request, 'main/about.html')
