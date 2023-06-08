from django.contrib import admin
from .models import Client, Employee, Posn, Service, Record, Location
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Client
    list_display = ("email", "first_name", "last_name", "phone",)
    list_filter = ("is_staff", "is_active",)
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
    search_fields = ("email", "phone")
    ordering = ("email",)

class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_filter = ["email", "phone", "posn__name"]
    list_display = ["email", "first_name", "last_name", "phone", "get_posn"]
    search_fields = ["email", "phone", "last_name", "first_name"]
    ordering = ["email",]

    def get_posn(self, obj):
        return obj.posn.name
    get_posn.admin_order_field  = 'posn'
    get_posn.short_description = 'position' 


admin.site.register(Client, CustomUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Posn)
admin.site.register(Service)
admin.site.register(Record)
admin.site.register(Location)
