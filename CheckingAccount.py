class CheckingAccount:
    def __init__(self, name, address, account_num, balance):
        """A CheckingAccount object is instantiated with attributes for customer name, address, account number, and total balance."""

        self.name = name
        self.address = address
        self.account_num = account_num
        self._balance = balance

    def __str__(self):
        """Returns a string showing the customer's name, address, account number, and balance."""

        return f"{self.name}, {self.address}, Account No: {self.account_num}, Balance: ${self._balance:.2f}"

    def debit(self, amount):
        """A debit transation decreases a customer's total balance and prints their new balance."""

        self._balance -= amount
        return f"${amount:.2f} has been subtracted from account. New balance is: ${self._balance:.2f}"

    def credit(self, amount):
        """A credit transaction increases a customer's total balance and prints their new balance."""

        self._balance += amount
        return f"${amount:.2f} has been added to account. New balance is: ${self._balance:.2f}"


def main():
    """Simulates a bank transaction."""

    # create a new instance of the CheckingAccount class
    new_customer = CheckingAccount('John Doe', '1234 Beach Street', 5555444, 500)

    print("Welcome to the bank!")
    # while transaction is in process
    while True:
        print("What would you like to do?")
        # choose what action to take
        action = input("Enter (b) for Balance, (w) for Withdraw, (d) for Deposit, (t) for Terminate Transaction: ").lower()
        # print balance
        if action == 'b':
            print(f"Balance is: ${new_customer._balance:.2f}")
        # withdraw money and print balance
        elif action == 'w':
            choice = float(input("How much would you like to withdraw? $"))
            new_customer.debit(choice)
            print(f"Balance is: ${new_customer._balance:.2f}")
        # deposit money and print balance
        elif action == 'd':
            choice = float(input("How much would you like to deposit? $"))
            new_customer.credit(choice)
            print(f"Balance is: ${new_customer._balance:.2f}")
        # break and exit current transaction
        elif action == 't':
            print("Thank you! Transaction terminated.")
            break
        # input was invalid, ask for input again
        else:
            print("Invalid input.")

main()


# ADDITIONAL TEST INFORMATION
# customer_2 = CheckingAccount('Jane Doe', '5678 Long Street', 6666333, 1000)
# print()
# print(customer_2.__str__())
# print(customer_2.credit(500))
# print(customer_2.debit(40))
# print(customer_2.credit(20.20))
# print(customer_2.debit(400.11))
