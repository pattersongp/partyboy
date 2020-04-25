from django import forms


class PartyForm(forms.Form):
    party_name = forms.CharField(label="Party Name", max_length=24)
