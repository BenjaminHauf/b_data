from django import forms
from .models import Address, Contact, Family

class AddressFormMixin(forms.ModelForm):
    street = forms.CharField(max_length=40)
    house_number = forms.IntegerField()
    addition = forms.CharField(required=False)
    room = forms.CharField(required=False)
    zip_code = forms.IntegerField()
    city = forms.CharField(max_length=30)
    state = forms.CharField(max_length=30)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, 'address') and self.instance.address:
            self.fields['street'].initial = self.instance.address.street
            self.fields['house_number'].initial = self.instance.address.house_number
            self.fields['addition'].initial = self.instance.address.addition
            self.fields['room'].initial = self.instance.address.room
            self.fields['zip_code'].initial = self.instance.address.zip_code
            self.fields['city'].initial = self.instance.address.city
            self.fields['state'].initial = self.instance.address.state

    def save(self, commit=True):
        address_data = {
            'street': self.cleaned_data['street'],
            'house_number': self.cleaned_data['house_number'],
            'addition': self.cleaned_data['addition'],
            'room': self.cleaned_data['room'],
            'zip_code': self.cleaned_data['zip_code'],
            'city': self.cleaned_data['city'],
            'state': self.cleaned_data['state'],
        }
        address, _ = Address.objects.get_or_create(**address_data)

        obj = super().save(commit=False)
        obj.address = address
        if commit:
            obj.save()
        return obj
    
class ContactFormMixin(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    contact_email = forms.CharField(max_length=30, required=False)
    contact_phone = forms.IntegerField(required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, 'contact') and self.instance.contact:
            self.fields['first_name'].initial = self.instance.contact.first_name
            self.fields['last_name'].initial = self.instance.contact.last_name
            self.fields['contact_email'].initial = self.instance.contact.contact_email
            self.fields['contact_phone'].initial = self.instance.contact.contact_phone
       

    def save(self, commit=True):
        contact_data = {
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'contact_email': self.cleaned_data['contact_email'],
            'contact_phone': self.cleaned_data['contact_phone'],

        }
        contact, _ = Contact.objects.get_or_create(**contact_data)

        obj = super().save(commit=False)
        obj.contact = contact
        if commit:
            obj.save()
        return obj

