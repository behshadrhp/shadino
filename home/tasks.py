from time import sleep
from celery import shared_task


@shared_task
def notify_customer(message):
    print('ایمیل ها ارسال شد')
    print(message)
    sleep(5)
    print('عملیات موفقیت امیز بود')
