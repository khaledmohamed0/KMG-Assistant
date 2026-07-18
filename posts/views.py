from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.select_related("client").order_by("-created_at")


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create.html"
    success_url = reverse_lazy("posts")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy("posts")