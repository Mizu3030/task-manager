from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'user')   # الأعمدة اللي هتظهر في لوحة الإدارة
    search_fields = ('title', 'description')     # البحث داخل المهام
    list_filter = ('period', 'user')             # فلترة حسب الفترة أو المستخدم
