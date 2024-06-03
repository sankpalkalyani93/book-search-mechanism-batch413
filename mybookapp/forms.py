from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    tags = forms.CharField(label='Tags', max_length=100)