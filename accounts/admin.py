from django.contrib import admin

# Register your models here.


from .models import Account
class AccountAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name", "birthdate")}
admin.site.register(Account, AccountAdmin)
