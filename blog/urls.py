from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
				path("", views.showposts),
				path("shrek/", views.shrek)
]