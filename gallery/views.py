from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image,Category
from django import forms
from cloudinary.forms import cl_init_js_callbacks      
from .forms import ImageForm

# Create your views here.

def gallery(request):
    image = Image.get_image()
    categories = Category.objects.all()
    return render(request, 'all-gallery/today-gallery.html',{"image":image,"categories":categories})

def gallery_by_category(request, category_id):
    images = Image.filter_by_category(category_id) 
    return render(request,'all-gallery/category.html',{"images":images}) 

def search_image(request):

    if 'gallery' in request.GET and request.GET["gallery"]:
        category= request.GET.get("gallery")
        searched_images =Image.search_image(category)
        message = f"{search_image}"

        return render(request, 'all-gallery/search.html',{"message":message, "gallery":searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'all-gallery/search.html',{"message":message})

def upload(request):
  context = dict( backend_form = ImageForm())

  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'today-gallery.html', context)
