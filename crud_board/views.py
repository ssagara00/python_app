from django.shortcuts import render

from .models import User

# Create your views here.


def list(request):
    context = {
        "users": User.objects.all().order_by("id"),
    }
    return render(request, "crud_board/list.html", context)
