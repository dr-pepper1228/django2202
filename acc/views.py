import re
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User
# Create your views here.

def index(request):
    return render(request,"acc/index.html")

def login_user(request):
    if request.method=="POST":
        un=request.POST.get("uname")
        up=request.POST.get("upass")
        user=authenticate(username=un,password=up)
        if user:
            login(request,user)
            return redirect("acc:index")
        else:
            pass
    return render(request,"acc/login.html")

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def signup(request):
    if request.method=="POST":
        un=request.POST.get("uname")
        up=request.POST.get("upass")
        uc=request.POST.get("ucomm")
        upic=request.FILES.get("upic")
        try:
            User.objects.create_user(username=un,password=up,comment=uc,pic=upic)
            return redirect("acc:login")
        except:
            pass
    return render(request,"acc/signup.html")

def profile(request):
    return render(request,"acc/profile.html")

def delete(request):
    request.user.pic.delete()
    request.user.delete()
    return redirect("acc:index")

def update(request):
    u=request.user
    if request.method=="POST":
        up=request.POST.get("upass")
        uc=request.POST.get("ucomm")
        um=request.POST.get("umail")
        upic=request.FILES.get("upic")
        if up:
            u.set_password(up)
        u.email=um
        u.comment=uc
        if upic:
            u.pic.delete()
            u.pic=upic
        u.save()
        login(request,u)
        return redirect("acc:profile")
    return render(request,"acc/update.html")