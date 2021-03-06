from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'postcode',
                  'country',
                  'county',
                  'email',
                  'phone_number',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
                'full_name': 'Full name',
                'street_address1': 'Street address 1',
                'street_address2': 'Street address 2',
                'town_or_city': 'Town or city',
                'county': 'County',
                'postcode': 'Postcode',
                'email': 'Email',
                'phone_number': 'Phone number',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if fields != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
