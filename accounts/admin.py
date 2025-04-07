from django.contrib import admin

from .models import Account, Family, Address
from .forms import AccountAdminForm, FamilyAdminForm
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm
    prepopulated_fields = {"slug": ("first_name", "last_name", "birthdate")}

class FamilyAdmin(admin.ModelAdmin):
    form = FamilyAdminForm
    
admin.site.register(Account, AccountAdmin)
admin.site.register(Family, FamilyAdmin)

