from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps

from .models import Party
from .forms import PartyForm

Image = apps.get_model('image', 'Image')


def index(request):
    latest_party_list = Party.objects.order_by("-created_at")[:5]
    context = {"latest_party_list": latest_party_list}
    return render(request, "party/index.html", context)


def detail(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    images = Image.objects.filter(party_id = party_id)
    print(images)

    return render(request, "party/detail.html", {"party": party})


def add_party(request):
    if request.method == "POST":

        form = PartyForm(request.POST)
        if form.is_valid():

            # insert a new Party into the db
            party = Party(**form.cleaned_data)
            party.save()

            return redirect('party:detail', party_id=party.id)
    else:
        form = PartyForm()

    return render(request, "party/add.html", {"partyForm": form})
