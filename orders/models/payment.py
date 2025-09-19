from zarinpal import Zarinpal
from zarinpal_utils.Config import Config


class ZarinpalPayment:
    def __init__(self, amount: int):
        if amount < 1000:
            raise ValueError("مبلغ پرداختی نباید کمتر از 1000 تومان باشد.")
        self.amount = amount * 10 # convert toman to rial
    
    def request(self):
