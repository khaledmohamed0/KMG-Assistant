from django.contrib import admin
from .models import Client, SocialAccount

admin.site.register(Client)

admin.site.register(SocialAccount)