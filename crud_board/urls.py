from django.urls import path

from .views import house_estimate, users

app_name = "crud_board"
urlpatterns = [
    # 一覧
    path("users", users.list, name="list"),
    path("users/new", users.edit, name="new"),
    path("users/edit/<int:id>", users.edit, name="edit"),
    path("users/show/<int:id>", users.show, name="show"),
    path("users/delete/<int:id>", users.delete, name="delete"),
    path("house_estimate/new", house_estimate.new, name="house_estimate_new"),
    path("house_estimate/", house_estimate.index, name="house_estimate_index"),
]
