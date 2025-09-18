from django.core.mail import EmailMessage
from laser_online_backend.settings import EMAIL_HOST_USER


def send_email(dest_address, template, *data):
    assert len(data)