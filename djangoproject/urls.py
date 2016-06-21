from django.conf.urls import url
from django.contrib import admin
from photos.views import HomeView, ListView
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
    url(r'^photos/$', ListView.as_view(), name='photos_list'),

    # Users URLS
    url(r'^login$', LoginView.as_view() , name='users_login'),
    url(r'^logout$', LogoutView.as_view() , name='users_logout')
]
