#  4. Class Variables and Class Methods

#  Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    # Class variable
    bank_name = "HBL"

    def __init__(self):
        print(f"I currently have an account with {Bank.bank_name} Bank.")


# class method
    @classmethod
    def change_bank_name(cls, name):
        # Change the 'bank_name'
        cls.bank_name = name
        print(f"I've recently opened another Bussiness account with {cls.bank_name} Bank.")


account1 = Bank()  # default name

# Change bank name
Bank.change_bank_name("bank of America")


account2 = Bank()  # updated name

          



