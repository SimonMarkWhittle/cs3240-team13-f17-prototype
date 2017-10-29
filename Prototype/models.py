from django.db import models

# Create your models here.



"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ModelFormWithFileField


def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})


def handle_uploaded_file(f):
    with open('upload.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
"""
