from django.contrib import admin
from accounts.models import Member,Custom_user
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ['custom_user','created_at']

admin.site.register(Member,MemberAdmin)