# 어드민 관련 설정 파일

from django.contrib import admin
from todolist.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_complete']
    list_display_links = ['id', 'title']
    list_filter = ['is_complete']

# admin.site.register(Todo, TodoAdmin)