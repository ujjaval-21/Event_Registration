from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "venue", "date", "time", "capacity", "created_by")
    list_filter = ("date", "created_at")
    search_fields = ("title", "venue", "created_by__username")
    readonly_fields = ("created_at",)
