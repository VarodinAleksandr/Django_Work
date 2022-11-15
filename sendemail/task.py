from celery import shared_task

from django.core.mail import send_mail


@shared_task
def add_sendmail(email, text_remainder):
    send_mail(
        'subject',
        text_remainder,
        'from@example.com',
        [email],
        fail_silently=False,
    )


def send_email(email, text_remainder):
    send_mail(
        'subject',
        text_remainder,
        'from@example.com',
        [email],
        fail_silently=False,
    )
