from django.db import models


class Client(models.Model):

    name = models.CharField(max_length=150)

    instagram_username = models.CharField(
        max_length=100,
        blank=True
    )

    facebook_page = models.CharField(
        max_length=150,
        blank=True
    )

    access_token = models.TextField()

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name