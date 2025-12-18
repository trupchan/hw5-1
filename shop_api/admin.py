from django.contrib import admin
from .models import UserConfirmation
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(UserConfirmation)
class UserConfirmationAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'created_at')
    search_fields = ('user__username', 'code')
    list_filter = ('created_at',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)