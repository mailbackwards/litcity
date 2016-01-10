import urllib
from bs4 import BeautifulSoup
import re
import requests
import string
from django.core.management.base import BaseCommand, CommandError
from app.models import Book, Quote

GOODREADS_API_KEY = "AL6GKEoebHFenfoDmtHuOA"

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('book_title', type=str)

    def handle(self, *args, **options):
        book_name = options['book_title']
        book = Book.objects.get(name=book_name)
        params = {
            'key': GOODREADS_API_KEY,
            'title': book_name,
        }
        r = requests.get('https://www.goodreads.com/book/title.xml',
            params=urllib.urlencode(params))
        soup = BeautifulSoup(r.text, 'html.parser')
        book_id = soup.find('book').find('work').find('id').text


        endpoint = 'https://www.goodreads.com/work/quotes/%s-%s/' % (
            book_id, book_name.replace(' ', '-'))
        r = requests.get(endpoint)
        soup = BeautifulSoup(r.text, 'html.parser')
        quotesPart = soup.findAll("div",attrs={'class': 'quoteText'})
        for quote in quotesPart:
            quote_text = quote.findNext('br').previousSibling
            cleaned_quote = quote_text.strip(string.whitespace)[1:-1]
            print 'Creating quote %s' % cleaned_quote
            quote = Quote.objects.create(text=cleaned_quote, book=book)
