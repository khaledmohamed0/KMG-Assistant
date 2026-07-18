import time

from django.core.management.base import BaseCommand

from scheduler.jobs import start


class Command(BaseCommand):

    help = "Run APScheduler"

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.SUCCESS("Scheduler Started...")
        )

        start()

        try:

            while True:

                time.sleep(1)

        except KeyboardInterrupt:

            self.stdout.write(
                self.style.WARNING("Scheduler Stopped.")
            )