from django.contrib import admin
from .models import Contact
from import_export.admin import ExportActionMixin


admin.site.site_title = "WerkBiz"
admin.site.site_header = "WerkBiz"


class ContactAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'company', 'is_reviewd']
    list_editable = ['is_reviewd']
    list_filter = ['is_reviewd']
    search_fields = ['full_name', 'phone', 'email', 'company']


admin.site.register(Contact, ContactAdmin)
