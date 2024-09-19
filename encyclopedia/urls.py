from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_entry", views.create_entry, name="create_entry"),
    path("<str:wiki_title>", views.entry, name="entry"),

]
