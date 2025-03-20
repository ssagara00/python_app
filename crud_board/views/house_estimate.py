from django.shortcuts import redirect, render

from crud_board.forms import HouseEstimateForm
from crud_board.models import HouseEstimate


def index(request):
    house_estimates = HouseEstimate.objects.all()
    return render(
        request, "house_estimate/index.html", {"house_estimates": house_estimates}
    )


def new(request):
    if request.method == "POST":
        form = HouseEstimateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crud_board:house_estimate_index")
    else:
        form = HouseEstimateForm()
    return render(request, "house_estimate/new.html", {"form": form})
