from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.db.models import Q
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



class CreateView(View):
    @method_decorator(login_required())
    def get(request):
        """
        Shows a form for a new photo
        :param request: HttpRequest
        :return: HttpResponse
        """

        if request.method=='GET':
            form=PhotoForm()

        form = PhotoForm()
        context = {
            'form' : form,
            'success_message' : ''
        }
        return render(request, 'photos/new_photo.html', context)


    @method_decorator(login_required())
    def post(request):
        """
        Shows a form for a new photo
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message=''
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


class ListView(View):
    def get(self, request):
        """
        :param request:
        :return:
        """
        if not request.user.is_authenticated():
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility = PUBLIC))
        context = {
            'photos':photos
        }
        return render(request, 'photos/photos_list.html', context)
