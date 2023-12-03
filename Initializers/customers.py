# Customer
# - `Customer __init__()`
#   - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
# - `Customer given_name()`
#   - returns the customer's given name
#   - should be able to change after the customer is created
# - `Customer family_name()`
#   - returns the customer's family name
#   - should be able to change after the customer is created
# - `Customer full_name()`
#   - returns the full name of the customer, with the given name and the family name concatenated, Western style.
# - `Customer all()`
#   - returns **all** of the customer instances
class Customer:
    all_customers = []
    count = 0

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.all_customers.append(self)
        Customer.count += 1

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers
    
    def __repr__(self):
        return f"<Customer: {self.full_name()}>"
    
