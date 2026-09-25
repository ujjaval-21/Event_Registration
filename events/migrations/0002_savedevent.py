from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("events", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="SavedEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("saved_at", models.DateTimeField(auto_now_add=True)),
                ("event", models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="saved_by", to="events.event")),
                ("user", models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="saved_events", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ("-saved_at",), "constraints": [models.UniqueConstraint(fields=("user", "event"), name="unique_saved_event")]},
        ),
    ]
