
from django.urls import path
from django.contrib import admin
from tempblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Myhomepage),
]