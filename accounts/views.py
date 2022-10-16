from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from accounts.forms import *
# Create your views here.
def index(request):
    return render(request,'index.html')


def Userlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')

        else:
            messages.error(request,"Username or Password is Incorrect")

    return render(request,"index.html")


def UserRegistration(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Successfuly created")
            return redirect("login")
        else:
            messages.error(request,"refill")
    context={
        "RegistrationForm":form
    }
    return render(request,"register.html",context)