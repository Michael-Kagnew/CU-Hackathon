from django.contrib import admin
from .models import Contract, JobTag

@admin.register(Contract, JobTag)
class ViewAdmin(admin.ModelAdmin):
    pass
