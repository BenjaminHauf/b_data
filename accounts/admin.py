from django.contrib import admin

from .models import Account, Family, Accommodation, Bank, InsuranceCategory, Insurance, Administration
from .forms import AccountAdminForm, FamilyAdminForm, AccommodationAdminForm, BankAdminForm, InsuranceAdminForm, AdministrationAdminForm
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm
    readonly_fields = ('slug',)
    
    fieldsets = (
        ('Account Information', {
            'fields': ('first_name', 'last_name', 'birthdate', 'slug', 'birthplace', 'image', 'phone_number')
        }),
        ('Address Details', {
            'fields': ('street', 'house_number', 'addition', 'room', 'zip_code', 'city', 'state',),
        }),
    )

class FamilyAdmin(admin.ModelAdmin):
    form = FamilyAdminForm

    fieldsets = (
        ('Family Information', {
            'fields': ('account', 'main_contact',)
        }),
        ('Contact Details', {
            'fields': ('first_name', 'last_name', 'contact_email', 'contact_phone',),
        }),
        ('Address Details', {
            'fields': ('street', 'house_number', 'addition', 'zip_code', 'city', 'state',),
        }),
    )

class AccommodationAdmin(admin.ModelAdmin):
    form = AccommodationAdminForm
    fieldsets = (
        ('Accommodations Information', {
            'fields': ('account', 'name',)
        }),
        ('Contact Details', {
            'fields': ('first_name', 'last_name', 'contact_email', 'contact_phone',),
        }),
        ('Payment Details', {
            'fields': ('iban', 'bic', 'sepa',),
        }),
        ('Address Details', {
            'fields': ('street', 'house_number', 'addition', 'zip_code', 'city', 'state',),
        }),
    )

class BankAdmin(admin.ModelAdmin):
    form = BankAdminForm
    fieldsets = (
        ('Accommodations Information', {
            'fields': ('account', 'company_name', 'iban', 'bic', 'start_date',)
        }),
        ('Contact Details', {
            'fields': ('first_name', 'last_name', 'contact_email', 'contact_phone',),
        }),
        ('Address Details', {
            'fields': ('street', 'house_number', 'addition', 'zip_code', 'city', 'state',),
        }),
    )

class InsuranceAdmin(admin.ModelAdmin):
    form = InsuranceAdminForm
    fieldsets = (
        ('Insurance Category', {
            'fields': ('category',)
        }),
        ('Insurance Information', {
            'fields': ('account', 'company_name', 'product','policy_number', 'start_date', 'end_date',)
        }),
        ('Payment Details', {
            'fields': ('iban', 'bic', 'sepa', 'reference'),
        }),
        ('Contact Details', {
            'fields': ('first_name', 'last_name', 'contact_email', 'contact_phone',),
        }),
        ('Address Details', {
            'fields': ('street', 'house_number', 'addition', 'zip_code', 'city', 'state',),
        }),
    )

class AdministrationAdmin(admin.ModelAdmin):
    form = AdministrationAdminForm
    fieldsets = (
        ('Account', {
            'fields': ('account',)
        }),
        ('Administration Information', {
            'fields': ('organisation', 'start_date',)
        }),
        ('Payment Details', {
            'fields': ('iban', 'bic', 'reference'),
        }),
        ('Contact Details', {
            'fields': ('first_name', 'last_name', 'contact_email', 'contact_phone',),
        }),
        ('Address Details', {
            'fields': ('street', 'house_number', 'addition', 'zip_code', 'city', 'state',),
        }),
    )


    
admin.site.register(Account, AccountAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Accommodation, AccommodationAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(InsuranceCategory)
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(Administration, AdministrationAdmin)
