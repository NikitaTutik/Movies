from django import forms

class MovieSearch(forms.Form):
    movie_name = forms.CharField(max_length=50,label='')