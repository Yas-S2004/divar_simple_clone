from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("شماره تلفن الزامی است")

        user = self.model(
            phone_number=phone_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, phone_number, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            phone_number,
            password,
            **extra_fields
        )
        
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=50, default="کاربر دیوار", blank=True, null=True)
    verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "phone_number"
    
    
    
    objects = UserManager()
