from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'name', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        ("User Credential", {'fields': ['email', 'password']}),
        ("personal info", {'fields': ['name']}),
        ("permissions", {'fields': ['is_admin']}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ['wide'],
                'fields': ['email', 'name', 'password1', 'password2']
            },
        ),
    ]
    search_fields = ['email']
    ordering = ['email', 'id']
    filter_horizontal = []


admin.site.register(User, UserModelAdmin)
