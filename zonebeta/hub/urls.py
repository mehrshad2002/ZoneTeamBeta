from django.urls import path
from . import views

urlpatterns = [
    path('' , views.HubIndex , name = "hub"),
    path('create/' , views.CreateIndex , name = "create") 
]