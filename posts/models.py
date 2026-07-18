from django.db import models
from django.contrib.auth.models import User
from clients.models import Client


class Post(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("scheduled", "Scheduled"),
        ("published", "Published"),
        ("failed", "Failed"),
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    image = models.ImageField(
        upload_to="posts/images/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="posts/videos/",
        blank=True,
        null=True
    )
    alt_text = models.CharField(
        max_length=200,
        blank=True,
        null = True,
    )

    idea = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    caption = models.TextField(
        blank=True
    )

    # بدل publish_date + publish_time
    publish_at = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_posts"
    )

    
    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.client.name} - {self.status}"