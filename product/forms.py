from django import forms
from django.forms import ModelForm
from . models import FabricSoftener, Traders


class SoftenerForm(ModelForm):
    class Meta:
        model = FabricSoftener
        fields = ('name', 'description', 'image_url', 'price', 'stock')
        labels = {
            'name': "",
            'description': "",
            'image_url': "",
            'price': "",
            'stock': "",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product description'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product image link here'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product price'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Totol product in stock'}),
        }


class TradersForm(ModelForm):
    class Meta:
        model = Traders
        fields = ('name', 'title', 'address', 'mobile_phone', 'country',
                  'proof_id', 'email', 'profile_picture', 'signup_date',)
        labels = {
            'name': "",
            'title': "",
            'address': "",
            'mobile_phone': "",
            'country': "",
            'proof_id': "",
            'email': "",
            'profile_picture': "",
            'signup_date': "",
        }
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'mobile_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country'}),
            'proof_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Identity type'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'select picture'}),
            'signup_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter date and time'}),
        }
