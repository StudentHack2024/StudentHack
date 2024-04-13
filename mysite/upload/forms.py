from django import forms

class image_input_form(forms.Form):
    image = forms.ImageField(label='Select a file')

