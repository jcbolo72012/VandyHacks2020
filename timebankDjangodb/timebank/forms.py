from django import forms
from .models import TempMember

class MemberForm(forms.ModelForm):

    class Meta:
        model = TempMember
        fields = ['fname', 'lname', 'email', 'passwd']
    