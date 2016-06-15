from django.http import HttpResponse
from django.shortcuts import render
from models import Photo

def home(request):
    photos = Photo.objects.all()
    context = {"photos_list": photos}
    return render(request, 'photos/home.html', context)

    #return HttpResponse(html)
