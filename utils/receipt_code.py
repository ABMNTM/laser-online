import random
import string


def generate_receipt_code():
    return ''.join(random.choices(string.digits, k=8))
