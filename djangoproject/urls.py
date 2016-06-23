from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from photos.views import HomeView, PhotoListView, UserPhotosView
from users.api import UserListAPI, UserDetailAPI
from users.views import LoginView
from users.views import LogoutView
from photos.views import DetailView
from photos.views import CreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Photo urls
    url(r'^$',HomeView.as_view(), name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$',DetailView.as_view(), name='photo_detail'),
    url(r'^photos/new$', CreateView.as_view(), name='photo_create'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_list'),
    url(r'^my-photos/$', login_required(UserPhotosView.as_view()), name='user_photos'),

    # Users URLS
    url(r'^login$', LoginView.as_view() , name='users_login'),
    url(r'^logout$', LogoutView.as_view() , name='users_logout'),

    #Users API
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name = 'user_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name = 'user_detail_api')
]
