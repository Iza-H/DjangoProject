from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from photos.forms import PhotoForm
from .models import Photo
from .models import PUBLIC

def home(request):
    """
    Show home page
    :param request: HttpRequest
    :return: HttpResponse
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {"photos_list": photos[:5]}
    return render(request, 'photos/home.html', context)
    #return HttpResponse(html)


def detail(request, pk):
    """
    Shows details page for the photo
    :param request: HttpRequest
    :param pk: id of the photo
    :return: HttpResponse
    """
    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos)==1 else None
    if photo is not None:
        context = {
            'photo':photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('Photo does not exist')


def create(request):
    """
    Shows a form for a new photo
    :param request: HttpRequest
    :return: HttpResponse
    """
    if request.method=='GET':
        form=PhotoForm()
    else:
        form=PhotoForm(request.POST)
        if form.is_valid():
            new_photo = form.save()

    form = PhotoForm()
    context = {
        'form' : form
    }
    return render(request, 'photos/new_photo.html', context)