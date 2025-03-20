from django.shortcuts import get_object_or_404, redirect, render

from crud_board.forms import UserForm
from crud_board.models import User

# Create your views here.


def list(request):
    context = {
        "users": User.objects.all().order_by("id"),
    }
    return render(request, "users/list.html", context)


def edit(request, id=None):

    if id:
        user = get_object_or_404(User, pk=id)
    else:
        user = User()

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("crud_board:list")
    else:
        form = UserForm(instance=user)

    # 新規・編集画面を表示
    return render(request, "users/edit.html", dict(form=form, id=id))


def delete(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == "POST":
        user.delete()
        return redirect("crud_board:list")


def show(request, id=id):
    user = get_object_or_404(User, pk=id)
    return render(request, "users/show.html", {"user": user})
