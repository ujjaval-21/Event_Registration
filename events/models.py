from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date", "time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"pk": self.pk})

    @property
    def available_seats(self):
        active_registrations = self.registrations.filter(status="active").count()
        return max(self.capacity - active_registrations, 0)


class SavedEvent(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="saved_events"
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="saved_by")
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-saved_at",)
        constraints = [
            models.UniqueConstraint(fields=("user", "event"), name="unique_saved_event")
        ]
