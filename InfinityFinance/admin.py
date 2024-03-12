from django.contrib import admin
from django.urls import path
from .models import Transaction

# Register your models here

admin.site.register(Transaction)