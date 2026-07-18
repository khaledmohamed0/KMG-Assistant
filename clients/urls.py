from django.urls import path

from .views import *

urlpatterns = [

    path("", ClientListView.as_view(), name="clients"),

    path("create/", ClientCreateView.as_view(), name="client_create"),

    path("<int:pk>/edit/", ClientUpdateView.as_view(), name="client_edit"),

    path("<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),

]