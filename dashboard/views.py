from django.views.generic import TemplateView
from clients.models import Client
from posts.models import Post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class DashboardView(TemplateView):

    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["clients_count"] = Client.objects.count()

        context["posts_count"] = Post.objects.count()

        context["scheduled_count"] = Post.objects.filter(
            status="scheduled"
        ).count()

        context["published_count"] = Post.objects.filter(
            status="published"
        ).count()

        context["latest_posts"] = Post.objects.order_by(
            "-created_at"
        )[:5]

        return context