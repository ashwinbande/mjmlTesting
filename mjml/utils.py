import json
import logging
import subprocess

from django.conf import settings
from django.core.mail import send_mail

LOGGER = logging.getLogger(__name__)


def get_context_for_template(file_name) -> dict:
    json_path = settings.BASE_DIR / f'templates/context/{file_name}.json'
    with open(json_path, 'r') as f:
        context = json.load(f)
        return context or {}


def transpile_mjml_to_html(file_name):
    mjml_path = settings.BASE_DIR / f'templates/mjml/{file_name}.mjml'
    email_path = settings.BASE_DIR / 'templates/email'
    p = subprocess.run(["mjml", mjml_path, "-o", email_path])
    if p.returncode != 0:
        LOGGER.error(f"Error transpiling {file_name}")
        return False
    return True


def get_email_settings():
    settings_path = settings.BASE_DIR / 'settings.json'
    with open(settings_path, 'r') as f:
        return json.load(f)


def send_email(html_message, file_name):
    mail_settings = get_email_settings()
    send_mail(
        message="",
        subject=f"testing email template: {file_name}",
        html_message=html_message,
        recipient_list=mail_settings.get("recipients"),
        from_email=mail_settings.get("auth_user"),
        auth_user=mail_settings.get("auth_user"),
        auth_password=mail_settings.get("auth_password"),
    )
    return mail_settings
