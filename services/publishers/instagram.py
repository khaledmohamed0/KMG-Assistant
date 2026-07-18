from django.conf import settings

from .base import BasePublisher
from social.apis.instagram_api import InstagramAPI


class InstagramPublisher(BasePublisher):

    def __init__(self):
        self.api = InstagramAPI()

    def publish(self, post):

        image_url = settings.SITE_URL + post.image.url

        container = self.api.create_container(
            image_url=image_url,
            caption=post.caption,
        )

        error = container.get("error")

        if error:
            raise Exception(error.get("message"))

        publish = self.api.publish_container(
            container["id"]
        )

        if "id" not in publish:
            raise Exception(
                publish.get("error", {}).get(
                    "message",
                    "Publish Failed"
                )
            )

        return publish