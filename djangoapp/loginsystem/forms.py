from django import forms
from .models import leave_request_form

class leave_request_form(forms.ModelForm):
    class Meta:
        model = leave_request_form
        fields = ('leave_type', 'start_date', 'end_date', 'reason')