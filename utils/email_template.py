from typing import Literal

EMAIL_TEMPLATE = {
    "admin_alert": {
        "name": "admin_alert.txt",
        "html": False,
        "arg_count": 1,
        "args": ["order"],
        "subject": "[New Order] A customer placed order {}"
    },
    "admin_payment_status": {
        "name": "admin_payment_status.txt",
        "html": False,
        "arg_count": 2,
        "args": ["order", "payment_status"],
        "subject": "[Payment Received] Order {}."
    },
    "customer_payment": {
        "name": "customer_payment.html",
        "html": True,
        "arg_count": 2,
        "args": ["order", "payment_link"],
        "subject": "Payment required for your order {}"
    },
    "payment_status": {
        "name": "payment_status.txt",
        "html": False,
        "arg_count": 2,
        "args": ["order", "payment_status"],
        "subject": "💳 Payment status for order {}"
    },
}

EmailType: Literal[
    "admin_alert", "admin_payment_status", "customer_payment", "payment_status"
]
