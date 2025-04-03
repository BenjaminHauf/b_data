from django.db import models
from django.utils.text import slugify

# Create your models here.
class Account(models.Model):
    
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    birthdate = models.DateField(null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True, default="")

    birthplace = models.CharField(max_length=30, null=True, blank=True)
    image = models.CharField(null=True,blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_account = Account.objects.get(pk=self.pk)
            if (old_account.first_name != self.first_name or
                old_account.last_name != self.last_name or
                old_account.birthdate != self.birthdate):
                self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.birthdate.strftime('%Y%m%d')}")
        else:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.birthdate.strftime('%Y%m%d')}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Family(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    address = models.CharField(max_length=30, null=True, blank=True)
    
    phone = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    main_contact = models.BooleanField(default=False)

    def __str__(self):
        if self.main_contact:
            return f" {self.account} -- {self.first_name} {self.last_name} - Main"
        else:
            return f" {self.account} -- {self.first_name} {self.last_name}"


class Accommodation(models.Model):

    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField()
    contact_name = models.CharField(max_length=30, null=True, blank=True)
    contact_email = models.CharField(max_length=30, null=True, blank=True)
    contact_phone = models.CharField(max_length=30, null=True, blank=True)


class Bank(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    account_number = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    iban = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField()
    contact = models.CharField(max_length=30, null=True, blank=True)
    contact_email = models.CharField(max_length=30, null=True, blank=True)
    contact_phone = models.CharField(max_length=30, null=True, blank=True)

class Insurance(models.Model):
    company_name = models.CharField(max_length=30, null=True, blank=True)
    product = models.CharField(max_length=30, null=True, blank=True)
    cost = models.CharField(max_length=30, null=True, blank=True)
    contact = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField()
    address = models.CharField(max_length=30, null=True, blank=True)
    contact_email = models.CharField(max_length=30, null=True, blank=True)
    contact_phone = models.CharField(max_length=30, null=True, blank=True)

class Administration(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    iban = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField()
    contact = models.CharField(max_length=30, null=True, blank=True)
    contact_email = models.CharField(max_length=30, null=True, blank=True)
    contact_phone = models.CharField(max_length=30, null=True, blank=True)
    reference_number = models.CharField(max_length=30, null=False, blank=False)
