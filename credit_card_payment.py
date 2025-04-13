from datetime import date
from payment_processor import PaymentProcessor


class CreditCardPayment(PaymentProcessor):
    def __init__(self, card_number: str, cvv: int, expiry_date: date):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date

    def process_payment(self, amount: float) -> bool:
        # Simulate payment processing by checking expiry_date
        if date.today() < self.expiry_date:
            print(f"Processed credit card payment of ${amount}")
            return True
        else:
            print("Credit card expired. Payment failed.")
            return False
