from django.shortcuts import render

from hub.models import Hubmodel
from .forms import HubForms

def HubIndex(request):

    return render(request, 'hub/hub.html')


def CreateIndex(request):
    my_form = HubForms()
    if request.method == "POST":
        my_form = HubForms(request.POST)
        if my_form.is_valid():
            Hubmodel.objects.create(**my_form.cleaned_data)
            my_form = HubForms()
    context = {
        "form" : my_form
    }
    return render(request, 'hub/create.html',context)
