from django.shortcuts import render

def HubIndex(request):
    return render(request, 'hub/hub.html')