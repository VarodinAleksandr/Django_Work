import logging

from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Author, Citaty


logger = logging.getLogger(__name__)


def pars_helper(page_number, count):
    r = requests.get(f'https://quotes.toscrape.com/page/{page_number}/')
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.select('div[class*="quote"]')
    if not articles:
        return {'count': count, 'quotes_exists': False}
    for i in articles:
        if count < 5:
            logger.info(f'get quote.count = {count}')
            logger.info(f'Page number {page_number}')
            author_name = i.find("small").get_text()
            # logger.info(f'Small {author_name}')
            quote_text = i.find("span").get_text()
            # logger.info(f'Span P{quote_text}')
            obj_a, created_a = Author.objects.get_or_create(name=author_name)
            obj_c, created_c = Citaty.objects.get_or_create(text=quote_text, author=obj_a)
            if created_c:
                count += 1
    return {'count': count, 'quotes_exists': True}


def send_email(email, text_remainder):
    send_mail(
        'subject',
        text_remainder,
        'from@example.com',
        [email],
        fail_silently=False,
    )


@shared_task
def pars_quotes():
    page_number = 1
    count = 0
    while count < 5:
        result = pars_helper(page_number, count)
        page_number += 1
        count = result.get('count')
        quotes_exists = result.get('quotes_exists')
        if not quotes_exists:
            logger.info('Task finished')
            send_email('admin@email.com', 'No new quotes was found. Task is over')
            return
