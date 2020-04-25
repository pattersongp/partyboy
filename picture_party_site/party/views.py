from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Party
from .forms import PartyForm


def index(request):
    latest_party_list = Party.objects.order_by("-created_at")[:5]
    context = {"latest_party_list": latest_party_list}
    return render(request, "party/index.html", context)


def detail(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    return render(request, "party/detail.html", {"party": party})


def add_picture(request, party_id):
    return HttpResponse("You're adding pictures to %s." % party_id)


def add_party(request):
    if request.method == "POST":

        form = PartyForm(request.POST)
        if form.is_valid():

            # insert a new Party into the db
            party = Party(**form.cleaned_data)
            party.save()

            return redirect(detail, party_id=party.id)
    else:
        form = PartyForm()

    return render(request, "party/add.html", {"partyForm": form})
