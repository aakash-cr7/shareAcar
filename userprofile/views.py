from django.shortcuts import render,render_to_response
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout, get_user_model
from .models import MyUser,journey
from forms import SignupForm,LoginForm,JourneyForm
from django.template import RequestContext
# Create your views here.
def home(request):
    if request.user.is_authenticated():
        upcoming_rides_list = journey.objects.order_by('time')
        current_user= request.user
        return render(request,'welcome.html',{'current_user':current_user.username,'upcoming_rides_list':upcoming_rides_list})
    else:
        text="Hello, anonymous"
        return render(request,'index.html',{'text':text})

def signup(request):
    if not request.user.is_authenticated():
        if request.method=="POST":
            form= SignupForm(request.POST)
            if form.is_valid():
                new_user = MyUser.objects.create_user(**form.cleaned_data)
                MyUser.backend='django.contrib.auth.backends.ModelBackend'
                authenticate()
                login(request,new_user) 
                #redirect, or however you want to get to the main view
                return HttpResponseRedirect('/')
        else:
            form = SignupForm()
        return render(request,'adduser.html',{'form':form})
    else:
        return HttpResponseRedirect('/')    

def user_login(request):
    if not request.user.is_authenticated():
        context = RequestContext(request)
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    authenticate()
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Your account is disabled")
            else:
                return HttpResponse("Invalid login")
        else:	
            return render_to_response("login.html",{},context)
    else:
        return HttpResponseRedirect('/')

def user_logout(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect("/")
	else:
		return HttpResponse("You have to be logged in before getting to logout.")



def addjourney(request):
    if request.user.is_authenticated():
        user=request.user
        context = RequestContext(request)
        if request.method == "POST":
            form = JourneyForm(request.POST)
            if form.is_valid():
                destination = form.cleaned_data['destination']
                time = form.cleaned_data['time']
                #user=request.user.username
                query = journey(destination =destination , time = time,user=user)
                query.save()
                return HttpResponseRedirect('/')
        else:
            form = JourneyForm()
        return render(request,'adduser.html',{'form':form})
    else:
        text="Please Login"
        return render(request,'index.html',{'text':text})
    
def profile(request):
    if request.user.is_authenticated():
        current_user= request.user
        return render(request,'profile.html',{'current_user':current_user})
    else:
        text="Hello, anonymous"
        return render(request,'index.html',{'text':text})


def about(request):
    return render(request,'about.html',{})