from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=40,
    widget=forms.TextInput(
    attrs={'class': 'input', 'placeholder': 'Name'}))
    email = forms.CharField(max_length=40,
    widget=forms.TextInput(
    attrs={'class': 'input', 'placeholder': 'Email'}))
    department = forms.CharField(max_length=40,
    widget=forms.TextInput(
    attrs={'class': 'input', 'placeholder': 'Department'}))
