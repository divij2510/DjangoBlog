from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def Myhomepage(request):
    query=request.GET.get('query')
    if query:
      searched=PersonalBlog.objects.filter(title__icontains=query)
    else:
      searched=PersonalBlog.objects.all()  
    posts=searched.order_by('-created_at')
    return render(request,'homepage.html',{'posts':posts})

@login_required
def MyBlogs(request):
    curr_user=request.user
    my_posts=PersonalBlog.objects.order_by('-created_at').filter(author=curr_user)
    return render(request,'MyBlogs.html',{'my_posts':my_posts})
@login_required
def PostBlog(request):
    if request.method=="POST":
        title=request.POST.get('title')
        image=request.FILES.get('image')
        body=request.POST.get('body')
        image_title=request.POST.get('image_title')
        author=request.user
        temp_blogpost=PersonalBlog(title=title,image=image,body=body,author=author,image_title=image_title)
        temp_blogpost.save()
        return redirect('Home')
    else:
     return render(request,'post.html',{})
def EditPost(request,postid):
    post=get_object_or_404(PersonalBlog,id=postid)
    oldpost=post
    context={'oldpost':oldpost}
    if request.method=="POST":
        post.title=request.POST.get('title')
        if request.FILES.get('image'):
         post.image=request.FILES.get('image')
        post.body=request.POST.get('body')
        post.image_title=request.POST.get('image_title')
        post.save()
        #messages.success(request,"Edit Successful!")
        return redirect('MyPage')
    return render(request,'editpost.html',context)
def DeletePost(request,postid):
        post=get_object_or_404(PersonalBlog,id=postid)
        post.delete()
        return redirect('MyPage')
        #return render(request,'',{}) 
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
            return redirect('Register')
        else:    
          new_user.save()
          messages.success(request,"Successfully Registered")
          return redirect('Register')

    return render(request,'register.html',{})

def Login(request):
 if request.method=="POST":
  username=request.POST.get('username')
  password=request.POST.get('password')
  new_auth=authenticate(request,username=username,password=password)
  if new_auth:
        login(request,new_auth)
        messages.success(request,"Successfully logged in")
        return redirect('new_Login')
  else:
        messages.error(request,"Wrong Username or password!")
        return redirect('new_Login')

 return render(request,'login.html',{}) 
       