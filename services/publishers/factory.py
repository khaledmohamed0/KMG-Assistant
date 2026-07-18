from .instagram import InstagramPublisher


class PublisherFactory:

    @staticmethod
    def get(account):

        if account.platform == "instagram":
            return InstagramPublisher()

        raise Exception("Platform Not Supported")