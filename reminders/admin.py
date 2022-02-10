from django.contrib import admin

from reminders.models import Reminders


@admin.register(Reminders)
class RemindersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday')
    list_display_links = ('name',)
    list_filter = ('name', 'birthday')
    search_fields = ('name', 'birthday')
