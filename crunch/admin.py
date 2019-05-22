from django.contrib import admin
from .models import ZohoInfo


class StudyDataAdmin(admin.ModelAdmin):
    model = ZohoInfo
    list_display = ['id', 'Company', ]
    ordering = ['-id', ]


admin.site.register(ZohoInfo, StudyDataAdmin)
