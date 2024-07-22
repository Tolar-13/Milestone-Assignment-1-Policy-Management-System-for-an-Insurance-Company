class Policyholder:
    def __init__(self, policyholder_id, name, status='active'):
        self.policyholder_id = policyholder_id
        self.name = name
        self.status = status
        self.policies = ""
        self.payments = 0

    def register_policyholder(self):
        self.status = 'active'
        print(f"Policyholder {self.name} registered.")

    def suspend_policyholder(self):
        self.status = 'suspended'
        print(f"Policyholder {self.name} suspended.")

    def reactivate_policyholder(self):
        self.status = 'active'
        print(f"Policyholder {self.name} reactivated.")

    def add_policy(self, policy):
        self.policies = policy

    def add_payment(self, payment):
        self.payments = payment

    def display_account_details(self):
        print(f"ID: {self.policyholder_id}, Name: {self.name}, Status: {self.status}")
        print("Policies:", self.policies)
        print("Payments:", self.payments)
