from django.utils import timezone

from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm


def post_list(request):
    posts = Person.objects.all().order_by("name")
    return render(request, 'npc/post_list.html', {'posts': posts})


def get_npc_id(request, npcid):
    npc = Person.objects.get(id=npcid)
    return render(request, 'npc/details.html', {'npc': npc})


def post_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('get_npc_id', npcid=post.pk)
    else:
        form = PersonForm
    return render(request, 'npc/post_edit.html', {'form': form})
