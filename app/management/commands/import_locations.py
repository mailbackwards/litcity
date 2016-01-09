import argparse
from django.core.management.base import BaseCommand, CommandError
from app.models import Location, Book
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('book_id', type=int)
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        book_id = options['book_id']
        book, created = Book.objects.get(pk=book_id)
        with open(options['csv'], 'r') as f:
            reader = csv.reader(f, lineterminator='\n')
            for row in reader:
                label, lat, lon = reader
                location, created = Location.objects.get_or_create(
                    lat=lat, lon=lon, label=label, book=book_id)
