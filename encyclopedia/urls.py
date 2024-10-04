from django.urls import path

from . import views

app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("create_entry/", views.create_entry, name="create_entry"),
    path("<str:wiki_title>/update_entry/", views.update_entry, name="update_entry"),
    path("<str:wiki_title>/", views.entry, name="entry"),
]
