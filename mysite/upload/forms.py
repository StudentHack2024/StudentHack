from django import forms

class image_input_form(forms.Form):
    image = forms.ImageField(label='Select an image', widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'image_input', "accept": 'image/*'}))