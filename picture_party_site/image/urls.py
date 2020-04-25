from django.urls import path

from . import views

app_name = "image"
urlpatterns = [
    # /image/add/1
    path("add/<int:party_id>", views.add_image, name="add_image"),
]
