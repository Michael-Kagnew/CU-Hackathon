from django.contrib import admin
from .models import Consultant, Client, Skill

@admin.register(Consultant, Client, Skill)
class ViewAdmin(admin.ModelAdmin):
    pass
