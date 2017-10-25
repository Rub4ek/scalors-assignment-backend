from django.core.mail import send_mail

from greatesttodo.celery import app
from reminder.models import Reminder


@app.task
def send_email_reminder(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        send_mail(
            subject=reminder.text,
            message=reminder.text,
            from_email=None,
            recipient_list=[reminder.email]
        )
    except Reminder.DoesNotExist:
        pass
