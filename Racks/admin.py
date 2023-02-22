from django.contrib import admin
from .models import RackModel


# Register your models here.
@admin.register(RackModel)
class RackAdmin(admin.ModelAdmin):
    list_display = ['name', 'ru', 'last_modified']
