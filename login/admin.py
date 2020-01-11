from django.contrib import admin
from .models import UserAccount

@admin.register(UserAccount)
class ViewAdmin(admin.ModelAdmin):
    pass
