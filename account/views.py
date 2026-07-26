from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from .models import User
from . import otp
import re

# Create your views here.
def register_or_login(request, phone):
    user = User.objects.filter(phone_number=phone).first()
    if user:
        login(request, user)
    else:
        user = User.objects.create_user(phone_number=phone)
        user.save()
    
    
    
def normalization_phone(phone):
    phone = phone.strip()
    
    if phone.startswith("+98"):
        phone = "0" + phone[3:]
    elif phone.startswith("98"):
        phone = "0" + phone[2:]
        
    return phone

      
      
def send_otp(request):
    message = ""
    
    if request.method == "POST":
        phone = request.POST.get("phone")
        phone_pattern = r"^(\+98|98|0)9\d{9}$"
        
        if phone:
            if re.fullmatch(phone_pattern, phone):
                normal_phone = normalization_phone(phone)
                otp.get_or_create_otp(normal_phone)
                request.session["phone"] = normal_phone
                
                return redirect("/account/register/verify/") 
            else:
                message = "شماره تلفن نامعتبر است"
        else:
            message = "لطفا شماره تلفن خود را وارد کنید"
        
    return render(request, "send_otp.html", {"message":message})
    
    
    
def verify_otp(request):
    message = ""
    phone = request.session.get("phone")
    ttl = otp.get_otp_ttl(phone)
    
    if request.method == "POST" and request.POST.get("code_request"):
        otp.resend_otp(phone)
        new_otp_ttl = otp.get_otp_ttl(phone)
        
        return JsonResponse({
            "success": True,
            "ttl": new_otp_ttl,
        })

    if request.method == "POST":
        received_otp = request.POST.get("otp")
        
        if received_otp:
            if otp.is_otp_valid(phone, received_otp):
                register_or_login(request, phone)
                otp.delete_otp(phone)
                del request.session["phone"]
                
                return redirect("/listings/")
            
            else:
                message = "کد وارد شده صحیح نیست"
        else:
            message = "لطفا کد تایید را وارد کنید"

    return render(request, "verify_otp.html",{"message": message, "ttl": ttl})
    
    
    
    