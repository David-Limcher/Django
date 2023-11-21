from django import forms

class YourForm(forms.Form):
    field1 = forms.CharField(label='Поле 1')
    field2 = forms.IntegerField(label='Поле 2')