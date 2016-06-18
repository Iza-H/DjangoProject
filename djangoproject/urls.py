from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Photo urls
    url(r'^$','photos.views.home', name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$','photos.views.detail', name='photo_detail'),

    # Users URLS
    url(r'^login$', 'users.views.login' , name='users_login'),
    url(r'^logout$', 'users.views.logout' , name='users_logout')
]
