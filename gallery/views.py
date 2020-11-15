from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image,Category

# Create your views here.
def gallery_today(request):
    return render(request, 'all-gallery/today-gallery.html')

def gallery(request):
    images = Image.get_images()
    categories = Category.objects.all()
    return render(request, 'all-gallery/today-gallery.html',{"images":images,"category":category})

def gallery_by_category(request, category_id):
    images = Image.filter_by_category(category_id) 
    return render(request,'all-gallery/category.html',{"images":images}) 

