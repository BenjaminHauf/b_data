from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Account

class AccountAdminForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=AdminDateWidget(attrs={'placeholder': 'DD MM YYYY'}),
        input_formats=['%d %m %Y', '%d.%m.%Y' ],
    )

    class Meta:
        model = Account
        fields = '__all__'