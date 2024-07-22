class Payment:
    def __init__(self, payment_id, policyholder_id, amount, date):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.amount = amount
        self.date = date

    def process_payment(self):
        print(f"Processing payment of {self.amount} for policyholder {self.policyholder_id}.")

    def send_reminder(self):
        print(f"Reminder: Payment of {self.amount} due for policyholder {self.policyholder_id}.")

    def apply_penalty(self):
        penalty = self.amount * 0.1  # Example penalty calculation
        print(f"Penalty of {penalty} applied to policyholder {self.policyholder_id}.")
