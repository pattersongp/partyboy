from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Party


def index(request):
    latest_party_list = Party.objects.order_by("-created_at")[:5]
    context = {'latest_party_list': latest_party_list}
    return render(request, 'party/index.html', context)

def detail(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    return render(request, 'party/detail.html', {'party': party})


def add_picture(request, party_id):
    return HttpResponse("You're adding pictures to %s." % party_id)
