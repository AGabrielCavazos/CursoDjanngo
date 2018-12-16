from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 
    #path del core
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('store/',views.store,name='store'),
    path('blog/',views.blog,name='blog'),
    path('sample/',views.sample,name='sample'),

]
