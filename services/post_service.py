from django.utils import timezone

from social.instagram.publisher import InstagramPublisher


class PostService:

    @staticmethod
    def publish(post):

        publisher = InstagramPublisher()

        success = publisher.publish(post)

        if success:

            post.status = "published"

            post.published_at = timezone.now()

            post.save()

        return success