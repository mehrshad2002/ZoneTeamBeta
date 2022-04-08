from django.shortcuts import render
from .forms import HubForms

def HubIndex(request):
    return render(request, 'hub/hub.html')


def CreateIndex(request):
    return render(request, 'hub/create.html')