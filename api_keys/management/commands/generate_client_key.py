__author__ = 'Taylor'

from django.core.management.base import BaseCommand
from api_keys.models import Client


class Command(BaseCommand):
    help = 'Generates an API key'
    args = '<client name>'

    def handle(self, *args, **options):
        name = args[0]
        client = Client(name=name)
        client.save()
        self.stdout.write('Created Key: {0} for client {1}'.format(client.key, name))