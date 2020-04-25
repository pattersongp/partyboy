from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps

from .models import Picture
from .forms import PictureForm

Party = apps.get_model('party', 'Party')

def add_picture(request, party_id):
    party = get_object_or_404(Party, pk=party_id)

    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():

            # insert a new Picture into the db
            picture_data = {**form.cleaned_data}
            picture_data["party_id"] = party

            picture = Picture(**picture_data)
            picture.save()

            return HttpResponse(f"You successfully added a picture to {party.party_name}")
        return HttpResponse(f"Something went wrong...")
    else:
        form = PictureForm()

    return render(request, "picture/add.html", {"party": party, "pictureForm": form})
