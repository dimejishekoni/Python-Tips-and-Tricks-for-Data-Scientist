class Customer:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        # Developer-friendly representation
        return f"Customer(name='{self.name}', age={self.age}, email='{self.email}')"

    def __str__(self):
        # User-friendly representation
        return f"Customer Profile: {self.name}, Age: {self.age}, Email: {self.email}"

# Create a customer base
customer1 = Customer("Alice Johnson", 30, "alice.johnson@example.com")
customer2 = Customer("Bob Smith", 45, "bob.smith@example.com")

# Print customer profiles using str and repr
print(customer1)  # Uses __str__ method
print(repr(customer2))  # Uses __repr__ method