from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'user')   # The columns that appear in the administration panel
    search_fields = ('title', 'description')     #Searching inside the oryx
    list_filter = ('period', 'user')             # Filters for period and user
