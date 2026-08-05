from django.contrib import admin
from .models import Listing, ListingImage, Category, Bookmark


# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
     readonly_fields = ["created_at", "updated_at", "seller"]
     
admin.site.register(ListingImage)

admin.site.register(Category)

admin.site.register(Bookmark)