from django.contrib import admin

from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("user", "event", "status", "registration_date")
    list_filter = ("status", "registration_date")
    search_fields = ("user__username", "event__title")
    list_select_related = ("user", "event")
