from django.shortcuts import redirect, render

from crud_board.forms import HouseEstimateForm
from crud_board.models import HouseEstimate


def new(request):
    if request.method == "POST":
        form = HouseEstimateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("house_estimate_list")
    else:
        form = HouseEstimateForm()
    return render(request, "house_estimate/new.html", {"form": form})
