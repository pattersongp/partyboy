from django.urls import path

from . import views

app_name = 'picture'
urlpatterns = [
    # /picture/add/1
    path("add/<int:party_id>", views.add_picture, name="add_picture"),
]

