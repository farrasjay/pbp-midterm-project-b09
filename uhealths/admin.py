import imp
from django.contrib import admin
from .models import UserProfileManger, UserProfile


# Register your models here.
admin.site.register(UserProfile)
    