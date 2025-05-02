from django.contrib import admin
from todo.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'is_completed']
    list_display_links = ['title']
    list_filter = ['is_completed']

    search_fields = ['title']
    # ordering = ['start_date']
    # fieldsets =
