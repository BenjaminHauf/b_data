from django.db import models
from django.utils.text import slugify

# Create your models here.
class Account(models.Model):
    
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    birthdate = models.CharField(max_length=10, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True)

    birthplace = models.DateField(max_length=30, null=True, blank=True)
    image = models.CharField(null=True,blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name}-{self.last_name}-{self.birthdate}")
            self.slug = base_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Family(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    address = models.CharField(max_length=30, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    main_contact = models.BooleanField(default=False)


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
