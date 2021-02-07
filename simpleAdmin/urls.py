from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('access/', Access.as_view(), name='access'),
    path('pinRemove/', PinRemove.as_view(), name='pinRemove'),
    path('pinAdd/', PinAdd.as_view(), name='pinAdd'),
    path('voiska/<id>', VoiskaEdit.as_view(), name='voiska'),
    path('voiskaDelete/', VoiskaDelete.as_view(), name='voiskaDelete'),
    path('voiskaAdd/', VoiskaAdd.as_view(), name='voiskaAdd'),
    path('authorDelete/', AuthorDelete.as_view(), name='AuthorDelete'),
    path('authorAdd/', AuthorAdd.as_view(), name='AuthorAdd'),
    path('', Main.as_view(), name='simpleAdminMain'),
    path('posts/<voiska>', Posts.as_view(), name='Posts'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
