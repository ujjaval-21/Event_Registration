from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from events.models import Event

from .models import Registration


@login_required
@require_POST
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    registration = Registration.objects.filter(user=request.user, event=event).first()

    if registration and registration.status == Registration.Status.ACTIVE:
        messages.error(request, "You are already registered for this event.")
        return redirect(event)

    active_registrations = event.registrations.filter(
        status=Registration.Status.ACTIVE
    ).count()
    if active_registrations >= event.capacity:
        messages.error(request, "This event is full.")
        return redirect(event)

    if registration:
        registration.status = Registration.Status.ACTIVE
        registration.registration_date = timezone.now()
        registration.save(update_fields=("status", "registration_date"))
        messages.success(request, "Your registration has been reactivated.")
    else:
        Registration.objects.create(user=request.user, event=event)
        messages.success(request, "You have registered for this event.")

    return redirect(event)


@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user).select_related(
        "event"
    )
    return render(request, "my_registrations.html", {"registrations": registrations})


@login_required
@require_POST
def cancel_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk, user=request.user)
    if registration.status == Registration.Status.CANCELLED:
        messages.error(request, "This registration has already been cancelled.")
    else:
        registration.status = Registration.Status.CANCELLED
        registration.save(update_fields=("status",))
        messages.success(request, "Your registration has been cancelled.")
    return redirect("registrations:my_registrations")
