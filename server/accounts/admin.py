from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'phone',
    )

    list_display_links = (
        'email',
    )

# admin.site.register(models.User, UserAdmin)