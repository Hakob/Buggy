from django.contrib import admin

from .models import Category, Bug


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['is_active']


class BugAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'title', 'category']
    readonly_fields = fields = [
        'created_at', 'title', 'category', 'assigned_to', 'created_by',
        'priority', 'state',
    ]
    date_hierarchy = 'created_at'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Bug, BugAdmin)
