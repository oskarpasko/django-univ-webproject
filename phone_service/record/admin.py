from django.contrib import admin
from .models import Client, Employee, Posn, Service, Record, Location
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Client
    list_display = ("email", "first_name", "last_name", "phone", "is_staff", "is_active",)
    list_filter = ("email", "first_name", "last_name", "phone", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name", "phone")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "email", "phone", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(Client, CustomUserAdmin)
admin.site.register(Employee)
admin.site.register(Posn)
admin.site.register(Service)
admin.site.register(Record)
admin.site.register(Location)
