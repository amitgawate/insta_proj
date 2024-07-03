from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']
