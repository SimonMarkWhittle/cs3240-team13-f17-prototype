from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.simple_upload, name='upload'),
]

#     url(r'^prototype/', include('Prototype.urls')),
