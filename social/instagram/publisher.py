from posts.models import Post


class InstagramPublisher:

    def publish(self, post):

        print("=" * 50)
        print("Publishing Post")
        print(f"Client : {post.social_accounts.first()}")
        print(f"Caption : {post.caption}")
        print("=" * 50)

        return True