from django import forms
from .models import Address, Family

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

