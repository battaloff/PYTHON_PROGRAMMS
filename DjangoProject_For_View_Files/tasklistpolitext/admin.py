from django.contrib import admin
from django.contrib.admin import ModelAdmin, AdminSite

from .models import TaskList

admin.site.site_header = 'POLITEXT'

admin.site.site_title = 'POLITEXT'

admin.site.index_title = 'POLITEXT'

admin.site.enable_nav_sidebar = False


@admin.register(TaskList)
class ModelAAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'qty',
        'file_name',
        'plate_size',
        'add_date_time',
        'equipment',
        'punch',
        'stage',
        'operator',
        'ready_datetime',

    ]

    list_display_links = [
        'company_name',
        'file_name'
    ]

    search_fields = [
        'company_name',
        'qty',
        'file_name',
        'plate_size',
        'equipment',
        'add_date_time',
        'punch',
        'stage',
        'operator',
        'ready_datetime',

    ]

    list_editable = [
        'punch',
        'stage',
        'equipment',
        'operator',
    ]

    list_filter = [
        'equipment',
        'add_date_time',
        'punch',
        'stage',
        'operator',
    ]
