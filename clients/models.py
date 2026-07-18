from django.db import models


class Client(models.Model):

    name = models.CharField(max_length=150)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SocialAccount(models.Model):

    PLATFORM_CHOICES = (

        ("instagram", "Instagram"),

        ("facebook", "Facebook"),

        ("linkedin", "LinkedIn"),

        ("twitter", "Twitter"),

    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="accounts"
    )

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES
    )

    username = models.CharField(
        max_length=150
    )

    page_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    access_token = models.TextField()

    refresh_token = models.TextField(
        blank=True,
        null=True
    )

    expires_at = models.DateTimeField(
        blank=True,
        null=True
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.client.name} - {self.platform}"