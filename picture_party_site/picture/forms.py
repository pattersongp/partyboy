from django import forms


class PictureForm(forms.Form):
    image = forms.ImageField(label="Picture to add")
