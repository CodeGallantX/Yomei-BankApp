from django.contrib import admin
from .models import Transaction

# Register your models here.

# Register Transaction model with the admin interface
admin.site.register(Transaction)
