from django.urls import path

from equipo import views

app_name = "equipo"
urlpatterns = [
    path("equipo", views.equipo, name="equipo-list"),
]