from django.urls import path
from filmyweb.views import wszystkie_filmy , nowy_film, edytuj_film

urlpatterns = [
    path('wszystkie/', wszystkie_filmy),
    path('nowy/', nowy_film),
    path('edytuj/<int:id>/', edytuj_film),
]