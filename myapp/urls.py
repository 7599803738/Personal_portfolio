from django.urls import path
from django.contrib import admin
from.import views
from django.urls import include, path
urlpatterns = [
    path('',views.home,name='home'),
]