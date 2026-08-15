from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path("register/", views.send_otp, name="send_otp"),
    path("register/verify/", views.verify_otp, name="verify_otp"),
    path("logout/", views.logout_user, name="logout"),
    path("user/profile/", views.user_profile, name="user_profile"),
    path("user/profile/edit/", views.edit_profile, name="edit_profile"),
    path("user/listings/", views.user_listings, name="user_listings"),
    path("user/bookmarks/", views.user_boomarks, name="user_bookmarks")
]
