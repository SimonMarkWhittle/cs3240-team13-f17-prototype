from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.simple_upload, name='upload'),
    url(r'^uploads\/(?P<name>[^.\\]+)(?P<ext>\.[^.\\]+)?$', views.display_upload, name='display_uploaded'),
]

#     url(r'^prototype/', include('Prototype.urls')),

