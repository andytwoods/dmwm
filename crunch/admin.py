from django.contrib import admin

from crunch.views import export
from .models import ZohoInfo


def exportToZoto(modelAdmin, request, queryset):
    return export(request, queryset)


exportToZoto.short_description = 'Download zoho compatible csv'


class StudyDataAdmin(admin.ModelAdmin):
    model = ZohoInfo
    list_display = ['id', 'Company', ]
    ordering = ['-id', ]
    actions = [exportToZoto, ]


admin.site.register(ZohoInfo, StudyDataAdmin)
