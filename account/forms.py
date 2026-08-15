from django import forms
from .models import User
from location.models import City

class EditProfileForm(forms.Form):
    username = forms.CharField(max_length=50)
    avatar = forms.ImageField(required=False)
    city = forms.ModelChoiceField(queryset=City.objects.all())
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.user = user
    def clean_username(self):
        username = self.cleaned_data["username"]
        
        if User.objects.filter(username=username).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError("این نام کاربری قبلا استفاده شده است")
        
        return username