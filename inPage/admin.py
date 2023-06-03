from django.contrib import admin

# Register your models here.
from .models import notes


@admin.register(notes)
class notesAdmin(admin.ModelAdmin):
    list_display = ('serial', 'title', 'desc')
