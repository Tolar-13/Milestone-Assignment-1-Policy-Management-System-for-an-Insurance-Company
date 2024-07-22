class Product:
    def __init__(self, product_id, name, description, status='active'):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.status = status

    def create_product(self):
        print(f"Product {self.name} created.")

    def update_product(self, name=None, description=None):
        if name and description:
            self.name = name
            self.description = description
        elif name:
            self.name = name
        elif description:
            self.description = description
        else:
            print("No updates provided.")
        print(f"Product {self.product_id} updated to Name: {self.name}, Description: {self.description}")

    def remove_product(self):
        self.status = 'removed'
        print(f"Product {self.name} removed.")
