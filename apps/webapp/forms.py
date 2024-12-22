from django import forms

from apps.webapp.models import PermohonanKredensial


class PermohonanKredensialForm(forms.ModelForm):
    class Meta:
        model = PermohonanKredensial
        fields = "__all__"


class IdentitasNakesForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    date_of_birth = forms.DateField(label="Date of birth")
    address = forms.CharField(label="Address", widget=forms.Textarea())
    profesi_nakes = forms.IntegerField(label="Profesi")
    nip_nps = forms.CharField(label="NIP/NPS", max_length=30, required=False)
    place_of_birth = forms.CharField(label="Place of birth", max_length=30)
    date_of_birth = forms.DateField(label="Date of birth")
    mobile_phone = forms.CharField(max_length=30)
    no_ijazah = forms.CharField(max_length=30, required=False)
    no_str = forms.CharField(max_length=30, required=False)
    no_sip = forms.CharField(max_length=30, required=False)
    starting_work = forms.DateField(label="Mulai bekerja", required=False)
