from django.core.management.base import BaseCommand
from location.models import Province, City
from pathlib import Path
import json


app_dir = Path(__file__).resolve().parent.parent.parent

json_path = app_dir / "data" / "iran_provinces_cities.json"

with open(json_path, "r", encoding="utf-8") as file:
    DATA = json.load(file)
  
    
class Command(BaseCommand):
    help = "Populate the database with provinces and cities."
    
    def handle(self, *args, **options):
        for province_name, cities in DATA.items():
        
            province, _ = Province.objects.get_or_create(name=province_name)
            
            
            for city_name in cities:
                City.objects.get_or_create(province=province, name=city_name)
    
                
        self.stdout.write(self.style.SUCCESS(f"Provinces and Cities loaded successfully."))