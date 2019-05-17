from django import forms

class CrunchForm(forms.Form):
    name = forms.CharField()
    data = forms.CharField(widget=forms.Textarea,)

