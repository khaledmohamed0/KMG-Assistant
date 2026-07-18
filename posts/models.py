from django.db import models
from clients.models import Client


class Post(models.Model):

    STATUS = (
        ("draft", "Draft"),
        ("scheduled", "Scheduled"),
        ("published", "Published"),
        ("failed", "Failed"),
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="posts/"
    )

    idea = models.CharField(
        max_length=500,
        blank=True
    )

    caption = models.TextField()

    publish_date = models.DateField()

    publish_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="draft"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.caption[:40]