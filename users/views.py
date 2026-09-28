from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from django.contrib.messages import get_messages
from .forms import LoginForm, RegistrationForm
from django.http import JsonResponse


def home(request):
    return render(request, "home.html")


def clear_messages(request):
    storage = get_messages(request)
    for _ in storage:
        pass



@login_required
def dashboard(request):
    from events.models import Event
    from registrations.models import Registration

    context = {
        "created_event_count": request.user.events.count(),
        "active_registration_count": request.user.registrations.filter(
            status=Registration.Status.ACTIVE
        ).count(),
        "upcoming_events": Event.objects.filter(
            date__gte=timezone.localdate()
        ).select_related("created_by")[:3],
    }
    return render(request, "dashboard.html", context)


def register(request):
    if request.user.is_authenticated:
        return redirect("users:dashboard")

    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)

        clear_messages(request)
        messages.success(request, "Your account has been created successfully.")
        return redirect("users:dashboard")

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("users:dashboard")

    form = LoginForm(request, data=request.POST or None)
    next_url = request.POST.get("next") or request.GET.get("next")

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())

        clear_messages(request)
        messages.success(request, "Welcome back!")
        
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure(),
        ):
            return redirect(next_url)
        return redirect("users:dashboard")

    return render(request, "login.html", {"form": form, "next": next_url})


@require_POST
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("users:login")


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def settings_view(request):
    return render(request, "settings.html")


def health(request):
    return JsonResponse({
        "status": "ok",
        "success": True,
        "message": "EventFlow Backend is healthy"
    })

