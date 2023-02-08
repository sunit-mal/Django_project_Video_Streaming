from django.contrib import admin
from django.urls import path,include
from TVApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('home/',views.homepage,name='homepage'),
    path('GoodByeMovie/',views.goodbye,name='goodbye'),
    path('Charlie/',views.charlie,name='charlie'),
    path('chup/',views.chup),
    path('freddy/',views.freddy),
    path('ghostStory/',views.ghoststory),
    path('about/',views.about,name='about'),
    path('login/',views.user_login,name='userlogin'),
    path('signup/',views.uesr_signup,name='usersignup'),
    path('logout/', views.user_logout, name='userlogout'),
    path('search/',views.search,name='search'),
]
