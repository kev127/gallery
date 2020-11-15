from django.urls import path
from . import views

urlpatterns=[
    path('',views.gallery_today,name = 'galleryToday'),
    path('search/', views.search_image, name='search_image')
]