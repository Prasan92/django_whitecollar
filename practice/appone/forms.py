from django import forms
from appone.models import User

class FormName(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
