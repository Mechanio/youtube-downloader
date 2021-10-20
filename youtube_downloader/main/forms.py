from django.forms import Form, CharField, TextInput


class SearchForm(Form):
    search_field = CharField(widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter URL'
        }))
