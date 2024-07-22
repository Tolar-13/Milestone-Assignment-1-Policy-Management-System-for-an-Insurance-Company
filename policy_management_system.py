from policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
product1 = Product(1, 'Health Insurance', 'Covers health-related expenses')
product2 = Product(2, 'Car Insurance', 'Covers car-related expenses')

# Register products
product1.create_product()
product2.create_product()

# Create policyholders
policyholder1 = Policyholder(1, 'Alade Adetola')
policyholder2 = Policyholder(2, 'Oluwatimileyin Samuel')

# Register policyholders
policyholder1.register_policyholder()
policyholder2.register_policyholder()

# Add policies to policyholders
policyholder1.add_policy(product1.name)
policyholder2.add_policy(product2.name)

# Process payments
payment1 = Payment(1, policyholder1.policyholder_id, 15000, '2024-07-21')
payment2 = Payment(2, policyholder2.policyholder_id, 700, '2024-07-21')

policyholder1.add_payment(payment1.amount)
policyholder2.add_payment(payment2.amount)

payment1.process_payment()
payment2.process_payment()

# Display account details
policyholder1.display_account_details()
policyholder2.display_account_details()
