from django.urls import path

from . import views

app_name = "crud_board"
urlpatterns = [
    # 一覧
    path("", views.list, name="list"),
    path("new", views.edit, name="new"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("show/<int:id>", views.show, name="show"),
    path("delete/<int:id>", views.delete, name="delete"),
]
