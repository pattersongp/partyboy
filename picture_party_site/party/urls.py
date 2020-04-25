from django.urls import path

from . import views

app_name = "party"
urlpatterns = [
    # /party/
    path("", views.index, name="index"),
    # /party/add/
    path("add/", views.add_party, name="add_party"),
    # /party/5/
    path("<int:party_id>/", views.detail, name="detail"),
]
