from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.event_list, name="list"),
    path("create/", views.create_event, name="create"),
    path("my-events/", views.my_events, name="my_events"),
    path("saved/", views.saved_events, name="saved"),
    path("<int:pk>/", views.event_detail, name="detail"),
    path("<int:pk>/save/", views.toggle_saved_event, name="toggle_saved"),
    path("<int:pk>/edit/", views.edit_event, name="edit"),
    path("<int:pk>/delete/", views.delete_event, name="delete"),
]
