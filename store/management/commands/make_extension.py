from django.db import connection
from django.core.management.base import BaseCommand
from django.contrib.postgres.operations import HStoreExtension


class Command(BaseCommand):
    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute('CREATE EXTENSION IF NOT EXISTS hstore;')

            cursor.execute('CREATE EXTENSION IF NOT EXISTS btree_gist;')

        self.stdout.write(
            self.style.SUCCESS("Extensions added successfully")
        )
