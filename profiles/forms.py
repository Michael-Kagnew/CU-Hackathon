from django import forms
from .models import Consultant, Client

class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        exclude = ('user',)
        fields = "__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)
        fields = "__all__"