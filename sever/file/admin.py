from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['userID', 'team', 'email']
    list_display_links = ['userID','team']

admin.site.register(User, UserAdmin)
