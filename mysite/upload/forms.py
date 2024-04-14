from django import forms

class image_input_form(forms.Form):
    image = forms.ImageField()

class email_input_form(forms.Form):
    email = forms.EmailField(label='Enter your email')


