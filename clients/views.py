from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Client
from .forms import ClientForm


class ClientListView(ListView):

    model = Client

    template_name = "clients/list.html"

    context_object_name = "clients"


class ClientCreateView(CreateView):

    model = Client

    form_class = ClientForm

    template_name = "clients/create.html"

    success_url = reverse_lazy("clients")


class ClientUpdateView(UpdateView):

    model = Client

    form_class = ClientForm

    template_name = "clients/create.html"

    success_url = reverse_lazy("clients")


class ClientDeleteView(DeleteView):

    model = Client

    template_name = "clients/delete.html"

    success_url = reverse_lazy("clients")