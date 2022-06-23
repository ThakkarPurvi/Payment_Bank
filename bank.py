from random import randint
from .customers import Customer
from .db import customers
from .validators import (validate_deposit, validate_withdrawal, validate_transfer)

def generate_customer_id() -> int:
    """Generates a random unique customer account number"""
    return randint(1000, 10000)

class Bank:
    @staticmethod
    def create(name: str) -> int:
        """Create a new customer and return account no"""
        customer = Customer(name, generate_customer_id())
        """Add to customers database"""
        customers[customer.account_number] = customer
        """Return Customer"""
        return customer.account_number

    @staticmethod
    def deposit(account_number: int, amount: int) -> None:
        """Deposit amount"""
        try:
            """Validate transaction"""
            customer = validate_deposit(account_number, amount)
            """Deposit amount"""
            customer._deposit(amount)
        except Exception as err:
            print(err)
        else:
            print(customer.balance)

    @staticmethod
    def withdraw(account_number: int, amount: int) -> None:
        """Withdraw amount"""
        try:
            """Validate transaction"""
            customer = validate_withdrawal(account_number, amount)
            """Withdraw amount"""
            customer._withdrawal(amount)
        except Exception as err:
            print(err)
        else:
            print(customer.balance)

    @staticmethod
    def transfer(account_1: int, account_2: int, amount: int) -> None:
        """Transfer amount from account_1 to account_2"""
        try:
            customer_1, customer_2 = validate_transfer(account_1, account_2, amount)
        except Exception as err:
            print(err)
        else:
            customer_1._withdrawal(amount)
            customer_2._deposit(amount)
            print("Transaction Successful")

    @staticmethod
    def balance(account_number: int) -> None:
        """View Balance"""
        customer = customers.get(account_number)
        if not customer:
            print("Invalid Customer")
            return
        print(customer.balance)