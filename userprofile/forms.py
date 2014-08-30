#from django.contrib.auth.models import User
from .models import MyUser,journey
from django.forms import ModelForm
#from django import forms 
class SignupForm(ModelForm):
    class Meta:
        model=MyUser
        fields=('username','email','password','workplace','mobile')
        
class LoginForm(ModelForm):        
    class Meta:
        model=MyUser
        fields=('username','password')


class JourneyForm(ModelForm):
    class Meta:
        model=journey
        fields=('destination','time')