from django.urls import path
from . import views


app_name = "account"

urlpatterns = [
    path("register/", views.send_otp, name="send_otp"),
    path("register/verify/", views.verify_otp, name="verify_otp"),
]
