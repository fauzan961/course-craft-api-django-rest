from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'gender', 'country', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    ordering = ('email',)
    
admin.site.register(User, CustomUserAdmin)
