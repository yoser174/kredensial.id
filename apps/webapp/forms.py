from django import forms
from .models import PermohonanKredensial


class PermohonanKredensialForm(forms.ModelForm):
    class Meta:
        model = PermohonanKredensial
        fields = "__all__"
