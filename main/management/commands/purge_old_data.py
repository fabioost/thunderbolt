from django.core.management.base import BaseCommand, CommandError
from  main.models import Area
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Delete objects older than 10 days'

    def handle(self, *args, **options):
        Area.objects.filter(area_data_ini_colheita__lte=datetime.now()-timedelta(days=30), area_ativa=False).delete()
        self.stdout.write('Deleted objects older than 10 days')