from django.http import HttpResponse
from django.shortcuts import render
from models import Photo

def home(request):
    photos = Photo.objects.all().order_by('-created_at')
    context = {"photos_list": photos[:5]}
    return render(request, 'photos/home.html', context)

    #return HttpResponse(html)
