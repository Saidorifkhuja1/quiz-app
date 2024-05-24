
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer
from django import forms
class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'are_you_teacher')

class CustomerUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'are_you_teacher')

class AccountSettingsForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name', 'email')

class EmailPreferencesForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('receive_newsletter', 'receive_notifications')

class DeleteAccountForm(forms.Form):
    confirm_deletion = forms.BooleanField(label='I confirm that I want to delete my account', required=True)
