from django import forms
from .models import CustomerInquiry


class CustomerInquiryForm(forms.ModelForm):

    service = forms.MultipleChoiceField(
        choices=[
            ('Sliding Window','Sliding Window'),
            ('Aluminium Door','Aluminium Door'),
            ('PVC Ceiling','PVC Ceiling'),
            ('Glass Work','Glass Work'),
            ('Other','Other'),
        ],
        widget=forms.CheckboxSelectMultiple
    )


    class Meta:

        model = CustomerInquiry

        fields = [
            'name',
            'mobile',
            'location',
            'service',
            'message',
        ]
