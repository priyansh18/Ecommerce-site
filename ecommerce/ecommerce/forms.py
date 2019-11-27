from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'name'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    Content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'message'}))


class LoginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput())   