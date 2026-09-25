from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import EventForm
from .models import Event, SavedEvent


def event_list(request):
    events = Event.objects.select_related("created_by")
    return render(request, "event_list.html", {"events": events})


def event_detail(request, pk):
    event = get_object_or_404(Event.objects.select_related("created_by"), pk=pk)
    is_saved = (
        request.user.is_authenticated
        and SavedEvent.objects.filter(user=request.user, event=event).exists()
    )
    return render(request, "event_detail.html", {"event": event, "is_saved": is_saved})


@login_required
def my_events(request):
    events = Event.objects.filter(created_by=request.user)
    return render(request, "my_events.html", {"events": events})


@login_required
def saved_events(request):
    saved_events = SavedEvent.objects.filter(user=request.user).select_related("event")
    return render(request, "saved_events.html", {"saved_events": saved_events})


@login_required
@require_POST
def toggle_saved_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    saved, created = SavedEvent.objects.get_or_create(user=request.user, event=event)
    if created:
        messages.success(request, "Event saved to your list.")
    else:
        saved.delete()
        messages.info(request, "Event removed from saved events.")
    return redirect(request.POST.get("next") or event)


@login_required
def create_event(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        event = form.save(commit=False)
        event.created_by = request.user
        event.save()
        messages.success(request, "Event created successfully.")
        return redirect(event)
    return render(request, "create_event.html", {"form": form})


def get_owned_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.created_by != request.user:
        raise PermissionDenied("You can only manage events you created.")
    return event


@login_required
def edit_event(request, pk):
    event = get_owned_event(request, pk)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Event updated successfully.")
        return redirect(event)
    return render(request, "edit_event.html", {"form": form, "event": event})


@login_required
@require_POST
def delete_event(request, pk):
    event = get_owned_event(request, pk)
    event.delete()
    messages.success(request, "Event deleted successfully.")
    return redirect("events:list")
