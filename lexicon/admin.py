from django.contrib import admin

# Register your models here.
from .models import Entry, Case


class CaseInline(admin.StackedInline):
	model = Case
	extra = 1


class EntryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, { 'fields': ['entry_name']}),
	]
	inlines = [CaseInline]

admin.site.register(Entry, EntryAdmin)