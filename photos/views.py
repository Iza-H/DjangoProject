from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View
from django.shortcuts import render
from photos.forms import PhotoForm
from .models import Photo
from .models import PUBLIC

class HomeView(View):
    def get(self, request):
        """
        Show home page
        :param request: HttpRequest
        :return: HttpResponse
        """
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {"photos_list": photos[:5]}
        return render(request, 'photos/home.html', context)
        #return HttpResponse(html)

class DetailView(View):
    def get(self, request, pk):
        """
        Shows details page for the photo
        :param request: HttpRequest
        :param pk: id of the photo
        :return: HttpResponse
        """
        possible_photos = Photo.objects.filter(pk=pk).select_related('owner')
        photo = possible_photos[0] if len(possible_photos)==1 else None
        if photo is not None:
            context = {
                'photo':photo
            }
            return render(request, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound('Photo does not exist')


@login_required()
def create(request):
    """
    Shows a form for a new photo
    :param request: HttpRequest
    :return: HttpResponse
    """
    success_message=''
    if request.method=='GET':
        form=PhotoForm()
    else:
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user #user authenticated
        form=PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save()
            form = PhotoForm() #a new clean form
            success_message = 'Photo saved correctlly'
            success_message += '<a href = "{0}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            success_message += 'Show photo'
            success_message += '</a>'

    form = PhotoForm()
    context = {
        'form' : form,
        'success_message' : success_message
    }
    return render(request, 'photos/new_photo.html', context)