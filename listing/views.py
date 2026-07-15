from django.shortcuts import render
from .models import Listing


# Create your views here.
def list_page(request):
    listings =  Listing.objects.all()
    
    return render(request, "list.html", {"listings":listings})