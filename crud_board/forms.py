import re

from django import forms
from django.forms import ModelForm

from crud_board.models import User


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
