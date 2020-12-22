from django.contrib import admin
from files.models import File
# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ['File_name', 'upload', 'file_type','created_at']
    list_filter = ["file_type"]

admin.site.register(File,FileAdmin)