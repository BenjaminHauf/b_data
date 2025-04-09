from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Account, Family
from .mixins import AddressFormMixin, ContactFormMixin

class AccountAdminForm(AddressFormMixin, forms.ModelForm):
    birthdate = forms.DateField(
        widget=AdminDateWidget(attrs={'placeholder': 'DD MM YYYY'}),
        input_formats=['%d %m %Y', '%d.%m.%Y' ],
    )

    class Meta:
        model = Account
        fields = (
            'first_name', 'last_name', 'birthdate', 'slug', 'birthplace', 'image',
            'phone_number', 'street', 'house_number', 'addition', 'room', 'zip_code', 'city', 'state'
        )
        

class FamilyAdminForm(AddressFormMixin, ContactFormMixin, forms.ModelForm):
    class Meta:
        model = Family
        exclude = ['address', 'contact']


