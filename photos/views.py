from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
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
