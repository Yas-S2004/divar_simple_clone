from django.urls import path
from . import views


app_name = "listing"

urlpatterns = [
    path('listings/', views.listing_page, name="list_page"),
    path("listings/<int:id>/", views.listing_detail, name="detail_page"),
    path("listings/create/", views.create_listing, name="create_listing")
]