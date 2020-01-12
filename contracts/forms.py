from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        exclude = ('applicants', 'team', 'status')
        fields = "__all__"

