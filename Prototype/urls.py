from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.simple_upload, name='upload'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

#     url(r'^prototype/', include('Prototype.urls')),

