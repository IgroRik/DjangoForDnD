from django.shortcuts import render

def post_list(request):
    return render(request, 'npc/post_list.html', {})