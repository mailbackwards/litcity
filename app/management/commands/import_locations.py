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
        book = Book.objects.get(pk=book_id)
        with open(options['csv_file'], 'r') as f:
            reader = csv.reader(f, lineterminator='\n')
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                label, lat, lon = row[0].encode('utf-8'), float(row[1]), float(row[2])
                print 'Creating location %s' % label
                location, created = Location.objects.get_or_create(
                    lat=lat, lon=lon, label=label, book_id=book_id)
