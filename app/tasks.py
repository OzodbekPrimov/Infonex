import urllib.parse
import urllib.request

from celery import shared_task
from django.conf import settings
from celery.utils.log import get_task_logger

from .models import Contact

logger = get_task_logger(__name__)


@shared_task
def send_contact_notification(contact_id: int) -> None:
    token = settings.BOT_TOKEN
    chat_id = settings.BOT_USER_ID
    if not token or not chat_id:
        logger.warning("BOT_TOKEN or BOT_USER_ID is not set; skipping notification")
        return

    try:
        contact = Contact.objects.get(id=contact_id)
    except Contact.DoesNotExist:
        logger.warning("Contact %s not found; skipping notification", contact_id)
        return

    message = (
        "New contact request:\n"
        f"Name: {contact.name}\n"
        f"Email: {contact.email}\n"
        f"Service: {contact.service}\n"
        f"Message: {contact.message}"
    )
    payload = urllib.parse.urlencode({"chat_id": chat_id, "text": message}).encode()
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        request = urllib.request.Request(url, data=payload)
        with urllib.request.urlopen(request, timeout=10) as response:
            if response.status != 200:
                body = response.read().decode("utf-8", errors="ignore")
                logger.error(
                    "Telegram API error %s: %s", response.status, body
                )
    except Exception:
        logger.exception("Failed to send Telegram notification")
