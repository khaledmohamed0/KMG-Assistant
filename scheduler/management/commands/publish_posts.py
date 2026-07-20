from django.core.management.base import BaseCommand
from scheduler.tasks import check_posts


class Command(BaseCommand):
    help = "Publish scheduled posts"

    def handle(self, *args, **kwargs):
        self.stdout.write("Checking scheduled posts...")
        check_posts()
        self.stdout.write(self.style.SUCCESS("Done."))