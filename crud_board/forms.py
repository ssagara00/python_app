import re

from django import forms
from django.forms import ModelForm

from crud_board.models import User

from .models import HouseEstimate


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "name",
            "email",
        )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if re.match(r".+@+", email) is None:
            raise forms.ValidationError("メールアドレスではありません。")
        return email


class HouseEstimateForm(forms.ModelForm):
    class Meta:
        model = HouseEstimate
        fields = [
            "estimate_company",
            "contact_person",
            "property_address",
            "estimate",
            "layout_memo",
            "sunlight_memo",
            "memo",
            "created_by",
            "updated_by",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.created_by:
            instance.created_by = User.objects.first()
        instance.updated_by = User.objects.first()
        if commit:
            instance.save()
        return instance
