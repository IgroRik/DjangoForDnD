from django.shortcuts import render
from .models import Person


def post_list(request):
    posts = Person.objects.all().order_by("name")
    return render(request, 'npc/post_list.html', {'posts': posts})
