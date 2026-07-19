from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Listing, ListingImage
from .forms import ListingForm


# Create your views here.
def listing_page(request):
    listings =  Listing.objects.all()
    
    return render(request, "list.html", {"listings":listings})



def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    images = ListingImage.objects.filter(listing=listing)
    
    return render(request, "detail.html", {"listing":listing, "images":images})



def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        valid_image_formats= ["image/jpeg", "image/jpg", "image/png"]
        uploading_image_errors = []
        
        if form.is_valid():
            if request.FILES:
                images = request.FILES.getlist("images")
                
                if len(images) > 10:
                   uploading_image_errors.append("حداکثر 10 تصویر قابل بارگذاری است") 
                    
                for image in images:
                    if image.size > 5 * 1024 * 1024:
                        uploading_image_errors.append("حجم تصویر نباید بیشتر از 5 مگابایت باشد")
                        
                            
                    if image.content_type not in valid_image_formats:
                        uploading_image_errors.append("فرمت تصویر معتبر نیست") 
                           
            else:
                uploading_image_errors.append("حداقل 1 تصویر باید بارگذاری شود")  
                     
            if len(uploading_image_errors) > 0:
                return render(request, "create_listing.html", {"form":form, "errors":uploading_image_errors})  
                                  
            cd = form.cleaned_data
            
            listing = Listing.objects.create(
                title=cd["title"],
                description=cd["description"],
                price=cd["price"],
                seller=request.user)
            
            listing.save()
            
            for image in images:
                listing_image = ListingImage.objects.create(listing=listing, image=image)
                listing_image.save()
                         
            return redirect("/listings/")         
    else:
        form = ListingForm()
        return render(request, "create_listing.html", {"form":form})
    