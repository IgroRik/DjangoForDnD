from django.conf.urls.static import static
from django.urls import path

from DjangoForDnD import settings
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('details/<int:npcid>/', views.get_npc_id, name='get_npc_id'),
    path('post/new/', views.post_new, name='post_new'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
