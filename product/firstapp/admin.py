from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     list_display = ['email', 'first_name', 'last_name', 'contact_number', 'is_staff']
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'gender', 'contact_number')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'middle_name', 'last_name', 'gender', 'contact_number', 'password1', 'password2'),
#         }),
#     )
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

admin.site.register(CustomUser)
