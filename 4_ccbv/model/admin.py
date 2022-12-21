from django.contrib import admin

from model.models import Verification


@admin.register(Verification)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')