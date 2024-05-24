from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
from .forms import CustomerCreationForm, CustomerUserChangeForm

class CustumerUserAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerUserChangeForm
    module = Customer
    list_display = ['username', 'first_name', 'last_name', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin. fieldsets + (
        (None, {'fields': ('age', 'is_teacher')}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'age', 'are_you_teacher')}),
    )


admin.site.register(Customer, CustumerUserAdmin)
