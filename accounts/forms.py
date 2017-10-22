from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, WeddingRole
from django.core.exceptions import ValidationError 


class UserRegistrationForm(UserCreationForm):

    forum_name = forms.CharField(max_length=50)
    wedding_role = forms.ModelChoiceField(queryset=WeddingRole.objects.all())
    email = forms.EmailField()

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
 
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'forum_name', 'wedding_role']
        exclude = ['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise forms.ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        # automatically set to email address to create a unique identifier
        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class AddPaymentDetailsForm(forms.ModelForm):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ['stripe_id']
