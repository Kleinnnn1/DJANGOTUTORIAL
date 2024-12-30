from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("polls/", include("django_polls.urls")),
    path("admin/", admin.site.urls),
    
] + debug_toolbar_urls()