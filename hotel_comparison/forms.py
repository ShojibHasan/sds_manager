from django import forms

class SearchForm(forms.Form):
    city = forms.CharField(max_length=100)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
    star_rating = forms.IntegerField(required=False, min_value=1, max_value=5)
