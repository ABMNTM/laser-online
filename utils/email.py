from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from laser_online_backend.settings import EMAIL_HOST_USER

from utils.email_template import EMAIL_TEMPLATE

from orders.models import Order


def send_email(dest_address, template, order: Order, *args):
    temp_data = EMAIL_TEMPLATE.get(template)
    assert temp_data is not None, "insert a valid value for 'template'."
    assert len(args) + 1 == temp_data.get("arg_count", 0), "arg counts are mismatch"

    subject = temp_data.get("subject").format(order.receipt_code)
    main_content = render_to_string(
        temp_data.get("name"),
        dict(zip(temp_data.get("args"), [order, *args])),
    )
    from_email = EMAIL_HOST_USER
    to = [dest_address]
    if temp_data.get("html"):
        # Plain text fallback
        text_content = f"The fallback of response."

        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(main_content, "text/html")
        msg.send()
    else:
        send_mail(subject, main_content, from_email, to)
