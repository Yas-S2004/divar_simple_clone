from django.urls import path
from . import views


app_name = "listing"

urlpatterns = [
    path('', views.list_page, name="list_page")
]