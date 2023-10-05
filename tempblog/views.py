from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

def Myhomepage(request):
    return render(request,'homepage.html',{})

def PostBlog(request):
    if request.method=="POST":
        title=request.POST.get('title')
        image=request.FILES.get('image')
        body=request.POST.get('body')
        author=request.user
        temp_blogpost=PersonalBlog(title=title,image=image,body=body,author=author)
        temp_blogpost.save()
        return redirect('Home')
    else:
     return render(request,'post.html',{})
def Register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email_id=request.POST.get('email_id')
        
        new_user=User(username=username,first_name=first_name,last_name=last_name,email=email_id)
        new_user.set_password( password )
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken!")
        else:    
         new_user.save()
         messages.success(request,"Successfully Registered")
         return redirect('Home')
    else:
      return render(request,'register.html',{})
def Login(request):
     username=request.POST.get('username')
     password=request.POST.get('password')
     new_auth=authenticate(request,username=username,password=password)
     if new_auth:
       login(request,new_auth)
       return redirect('Home')
     return render(request,'login.html',{}) 
       