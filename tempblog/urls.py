
from django.urls import path
from django.contrib import admin
from tempblog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Myhomepage,name='Home'),
    path('post/',views.PostBlog,name='Post'),
    path('signup/',views.Register,name='Register'),
    path('login/',views.Login,name='new_Login'),
    path('userpage/',views.MyBlogs,name='MyPage'),
    path('userpage/editpost/<int:postid>',views.EditPost,name='PostEdit'),
    path('userpage/deletepost/<int:postid>',views.DeletePost,name='PostDelete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)