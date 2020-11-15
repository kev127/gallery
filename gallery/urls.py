from django.urls import path
from . import views

urlpatterns=[
    path('',views.gallery_today,name = 'galleryToday'),
    path('search/', views.search_image, name='search_image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)