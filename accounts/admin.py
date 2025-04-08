from django.contrib import admin

from .models import Account, Family, Address
from .forms import AccountAdminForm, FamilyAdminForm
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

    
admin.site.register(Account, AccountAdmin)
admin.site.register(Family, FamilyAdmin)

