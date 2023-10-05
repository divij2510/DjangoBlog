
from django.urls import path
from django.contrib import admin
from tempblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Myhomepage,name='Home'),
    path('post/',views.PostBlog,name='Post'),
    path('signup/',views.Register,name='Register'),
    path('login/',views.Login,name='Login'),
    
]