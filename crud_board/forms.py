from django.forms import ModelForm

from crud_board.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            "name",
            "email",
        )
