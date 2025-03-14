from django.urls import path

from . import views

app_name = "crud_board"
urlpatterns = [
    # 一覧
    path("", views.list, name="list"),
]
