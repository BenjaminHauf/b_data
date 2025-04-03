from django.contrib import admin

from .models import Account, Family
from .forms import AccountAdminForm
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm
    prepopulated_fields = {"slug": ("first_name", "last_name", "birthdate")}
admin.site.register(Account, AccountAdmin)
admin.site.register(Family)
