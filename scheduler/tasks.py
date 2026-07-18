from django.utils import timezone

from posts.models import Post
from services.post_service import PostService


def check_posts():

    posts = Post.objects.filter(
        status="scheduled",
        publish_at__lte=timezone.now()
    )

    for post in posts:

        PostService.publish(post)