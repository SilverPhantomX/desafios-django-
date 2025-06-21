from django.urls import path
from . import views


urlpatterns = [
    path("saludo_fijo/",views.saludo),
    path("saludo/<str:nombre>/",views.saludo_nombre),
    path("edad/<int:edad>/",views.edad),
    path("", views.inicio, name="inicio"),
    path("curriculum/", views.curriculum, name="curriculum")
]