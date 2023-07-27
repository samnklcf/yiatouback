from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile

class UserAdminConfig(UserAdmin):
    search_fields = ['last_name', 'first_name', 'email', 'username']
    list_filter = ['last_name', 'first_name', 'email', 'username', 'is_staff', 'is_superuser', 'is_verified']
    ordering = ('-created_at',)
    list_display = ('last_name', 'first_name', 'email', 'username', 'is_staff', 'is_verified', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('last_name', 'first_name', 'email', 'username')}),
        ('Permission', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('last_name', 'first_name', 'email', 'username', 'password1', 'password2', 'is_active', 'is_staff')
        }), 
    )

admin.site.register(User, UserAdminConfig)
admin.site.register(UserProfile)