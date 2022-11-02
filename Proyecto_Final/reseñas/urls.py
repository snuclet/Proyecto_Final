from django.urls import path

from reseñas import views

app_name = "reseñas"
urlpatterns = [
    path("reseñas", views.reseña, name="reseña-list"),
]