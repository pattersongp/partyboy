from django.urls import path

from . import views

urlpatterns = [
    # /party/
    path("", views.index, name="index"),
    # /party/add/
    path("add/", views.add_party, name="add_party"),
    # /party/5/
    path("<int:party_id>/", views.detail, name="detail"),
    # /party/5/add/
    path("<int:party_id/add/>", views.add_picture, name="add_picture"),
]