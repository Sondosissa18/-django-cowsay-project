from django import forms

# from cowsay_app.models import Cowtext


class NameForm(forms.Form):
    text = forms.CharField(label='Text', max_length=100)