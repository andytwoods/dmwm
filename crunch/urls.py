from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from crunch import views

urlpatterns = [
    path("", views.Crunch.as_view(), name="crunch"),
    path("export/", views.export, name="export")
]
