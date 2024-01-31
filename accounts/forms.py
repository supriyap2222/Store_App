from django import forms
from .models import Account

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password', 'class':'form-control'}))
    
    # we r entering next 4 lines to get css in form input box
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter First Name', 'class':'form-control'}))
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name', 'class':'form-control'}))
    email       = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    phone_number= forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Phone Number', 'class':'form-control'}))

    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']

    # to make sure password and confirm password is same or not
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password            = cleaned_data.get('password')
        confirm_password    = cleaned_data.get('confirm_password')
    
        if password != confirm_password:
            raise forms.ValidationError(
                "!!! Password doesnot matched!!!!"
            )