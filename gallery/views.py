from django.http import HttpResponse 
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect

# Create your views here.
def gallery_today(request):
    return render(request, 'all-gallery/today-gallery.html')

