from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ViewAdmin(admin.ModelAdmin):
    pass
