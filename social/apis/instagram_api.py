from django.conf import settings

from .base_api import BaseAPI


class InstagramAPI(BaseAPI):

    BASE_URL = "https://graph.facebook.com/v25.0"

    def create_container(self, image_url, caption):

        return self.post(
            f"{self.BASE_URL}/{settings.INSTAGRAM_BUSINESS_ID}/media",
            {
                "image_url": image_url,
                "caption": caption,
                "access_token": settings.INSTAGRAM_ACCESS_TOKEN,
            },
        )

    def publish_container(self, creation_id):

        return self.post(
            f"{self.BASE_URL}/{settings.INSTAGRAM_BUSINESS_ID}/media_publish",
            {
                "creation_id": creation_id,
                "access_token": settings.INSTAGRAM_ACCESS_TOKEN,
            },
        )