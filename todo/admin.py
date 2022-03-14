from django.contrib import admin
from .models import *
# Register your models here.


class MyAdminSite(admin.AdminSite):
	admin.AdminSite.site_header = "Admin Access"
	admin.AdminSite.site_title = "Django"


@admin.register(task)
class taskAdmin(admin.ModelAdmin):
	list_display = ('completed', 'priority', 'title', 'notes', 'due_time', 'due_date', 'completed_on')
	list_filter = ('completed', 'completed_on', 'priority')
	list_per_page = 10
	search_fields = ('title', )

	# fields = ('title', 'priority', 'notes', 'due', ('completed', 'completed_on'))

	fieldsets = (
		(None, {'fields': ('title', 'priority')}),
		('Extra Detail', {'fields': ('notes', 'due_time', 'due_date')}),
		('Completion', {'fields': ('completed', 'completed_on')})
	)
