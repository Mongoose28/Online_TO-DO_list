from django import forms
from list.models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["task","completed"]
