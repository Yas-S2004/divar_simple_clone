from django.db import models
from account.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name="category"
        verbose_name_plural="categories"
        
        
    def __str__(self):
        return self.name
  
    
class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
    price = models.DecimalField(max_digits=9, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listing")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f"{self.title} - {self.seller}" 
    
    
    
class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="listing/%Y.%m.%d")
    
    
    def __str__(self):
        return f"{self.listing} images"
    
    
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmark")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookmark")
      
    def __str__(self):
        return self.listing.title    
