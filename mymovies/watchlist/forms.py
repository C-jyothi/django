from django import forms

class MovieForm(forms.Form):
    movie_name = forms.CharField(max_length=100)
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )