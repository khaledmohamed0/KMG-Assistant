from django.utils import timezone

from services.publishers.factory import PublisherFactory


class PostService:

    @staticmethod
    def publish(post):

        try:

            for account in post.social_accounts.all():

                publisher = PublisherFactory.get(account)

                result = publisher.publish(post)

                post.platform_post_id = result["id"]

            post.status = "published"
            post.published_at = timezone.now()
            post.notes = ""

        except Exception as e:

            post.status = "failed"
            post.notes = str(e)

        post.save()