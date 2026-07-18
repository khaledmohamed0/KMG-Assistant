from apscheduler.schedulers.background import BackgroundScheduler

from .tasks import check_posts

scheduler = BackgroundScheduler()


def start():

    if scheduler.running:
        return

    scheduler.add_job(
        check_posts,
        trigger="interval",
        seconds=30,
        id="check_posts",
        replace_existing=True,
    )

    scheduler.start()

    print("Scheduler Running...")