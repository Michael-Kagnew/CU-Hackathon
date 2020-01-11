from django.contrib import admin
from .models import Consultant, Client

@admin.register(Consultant, Client)
class ViewAdmin(admin.ModelAdmin):
    pass
