from django import forms

class image_input_form(forms.Form):
    image = forms.ImageField(label='Select a file')

class email_input_form(forms.Form):
    email = forms.EmailField(label='Enter your email')


