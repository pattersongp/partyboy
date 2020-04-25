from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps

from .models import Image
from .forms import ImageForm

Party = apps.get_model('party', 'Party')

def add_image(request, party_id):
    party = get_object_or_404(Party, pk=party_id)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():

            # insert a new Image into the db
            image_data = {**form.cleaned_data}
            image_data["party_id"] = party

            image = Image(**image_data)
            image.save()

            return HttpResponse(f"You successfully added a image to {party.party_name}")
        return HttpResponse(f"Something went wrong...")
    else:
        form = ImageForm()

    return render(request, "image/add.html", {"party": party, "imageForm": form})
