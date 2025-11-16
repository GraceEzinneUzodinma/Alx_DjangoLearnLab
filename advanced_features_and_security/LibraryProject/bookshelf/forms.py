# forms.py
from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=True,
        label="Book Title",
        widget=forms.TextInput(attrs={'placeholder': 'Enter book title'})
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        label="Author",
        widget=forms.TextInput(attrs={'placeholder': 'Enter author name'})
    )
    publication_year = forms.IntegerField(
        required=True,
        label="Publication Year",
        min_value=0,    # optional: prevent negative years
        max_value=2100, # optional: reasonable upper limit
        widget=forms.NumberInput(attrs={'placeholder': 'Enter publication year'})
    )
