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

class LocationAdmin(admin.ModelAdmin):
    list_filter = ["country", "city"]
    list_display = ["country", "city", "street", "number", "postcode", "phone"]
    search_fields = ["country", "city", "street", "number", "postcode", "phone"]
    ordering = ["country", "city", "street", "number"]

class PosnAdmin(admin.ModelAdmin):
    list_display = ["name", "salary"]
    search_fields = ["name", "salary"]
    ordering = ["-salary", "name"]    

class RecordAdmin(admin.ModelAdmin):
    model = Record
    list_filter = ["price","start_date", "deadline"]
    list_display = ["client", "get_service", "price", "start_date", "deadline", "get_location"]
    search_fields = ["client", "get_service", "price", "start_date", "deadline", "location__city"]
    ordering = []
    date_hierarchy = 'deadline'

    def get_service(self, obj):
        return obj.service.name
    get_service.admin_order_field  = 'service'
    get_service.short_description = 'service' 
    def get_location(self, obj):
        return f'{obj.location.city}, {obj.location.street} {obj.location.number}'
    get_service.admin_order_field = 'location'
    get_service.short_description = 'location'

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name", "price"]
    ordering = ["-price", "name"]

admin.site.register(Client, CustomUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Posn, PosnAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Location, LocationAdmin)
