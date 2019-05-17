from django.contrib import admin
from .models import Info


class StudyDataAdmin(admin.ModelAdmin):
    model = Info
    list_display = ['Company_Name', 'Employees', ]


admin.site.register(Info, StudyDataAdmin)
