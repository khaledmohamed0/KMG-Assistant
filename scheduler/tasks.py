from django.utils import timezone

from posts.models import Post
from services.post_service import PostService




def check_posts():

    print("Current Time:", timezone.localtime())

    posts = Post.objects.filter(
        status="scheduled",
        publish_at__lte=timezone.now()
    )

    print("Found:", posts.count())

    for post in Post.objects.all():
        print(
            post.id,
            post.status,
            post.publish_at,
            
        )

    for post in posts:
        print("Publishing:", post.id)
        PostService.publish(post)