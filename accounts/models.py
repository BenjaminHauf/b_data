from django.db import models
from django.utils.text import slugify

# Create your models here.
class Address(models.Model):

    street = models.CharField(max_length=30, null=True, blank=True)
    house_number = models.IntegerField(null=True, blank=True)
    addition = models.CharField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return f"{self.street} {self.house_number}{self.addition} {self.zip_code} {self.city}"
    

class Contact(models.Model):

    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    contact_email = models.CharField(max_length=30, null=True, blank=True)
    contact_phone = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name}{self.last_name} {self.contact_email} {self.contact_phone}"


class Account(models.Model):
    
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    birthdate = models.DateField(null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True, default="")

    birthplace = models.CharField(max_length=30, null=True, blank=True)
    image = models.CharField(null=True,blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)

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
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.SET_NULL)
    main_contact = models.BooleanField(default=False)

    def __str__(self):
        if self.main_contact:
            return f" {self.account} -- {self.first_name} {self.last_name} - Main"
        else:
            return f" {self.account} -- {self.first_name} {self.last_name}"


class Accommodation(models.Model):

    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.SET_NULL)
    cost = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField()

class Bank(models.Model):
    company_name = models.CharField(max_length=30, null=True, blank=True)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    account_number = models.CharField(max_length=30, null=True, blank=True)
    iban = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField()

class Insurance(models.Model):
    company_name = models.CharField(max_length=30, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.CharField(max_length=30, null=True, blank=True)
    cost = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField()

class Administration(models.Model):
    organisation = models.CharField(max_length=30, null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.SET_NULL)
    iban = models.CharField(max_length=30, null=True, blank=True)
    start_date = models.DateField()
    reference_number = models.CharField(max_length=30, null=False, blank=False)