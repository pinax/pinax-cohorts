from django import forms

from .models import Cohort


class CohortCreateForm(forms.ModelForm):

    class Meta:
        model = Cohort
        fields = ["name"]
