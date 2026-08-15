from django.db import models

# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    
      
class City(models.Model):
    name = models.CharField(max_length=20)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="cities")
    
    class Meta:
        unique_together = ("province", "name")
        
    def __str__(self):
        return self.name