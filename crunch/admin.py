from django.contrib import admin
from .models import ZohoInfo


class StudyDataAdmin(admin.ModelAdmin):
    model = ZohoInfo
    list_display = ['Company',]


admin.site.register(ZohoInfo, StudyDataAdmin)
