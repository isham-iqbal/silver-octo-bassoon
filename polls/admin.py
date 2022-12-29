from django.contrib import admin

from polls.models import Bar

class BarAdmin(admin.ModelAdmin):
    model = Bar

    fields = (
        "value",
    )

    list_display = (
        "value",
    )

admin.site.register(Bar, BarAdmin)