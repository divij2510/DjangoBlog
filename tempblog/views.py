from django.shortcuts import render

def Myhomepage(request):
    return render(request,'homepage.html',{})
