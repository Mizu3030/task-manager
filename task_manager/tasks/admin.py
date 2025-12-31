from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'period', 'due_date', 'user')
    list_filter = ('status', 'period', 'due_date', 'user')
    search_fields = ('title', 'description')
    ordering = ('status', 'due_date')
