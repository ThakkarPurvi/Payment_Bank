from . import criteria
from . import errors
from . customers import Customer
from . db import customers

def get_customer(account_number: int) -> Customer:
    """Retrieve the customer"""
    customer = customers.get(account_number)
    if not customer:
        raise errors.Invalid_Customer_Error(f"Account No: {account_number} does not exist.")
    return customer

def check_validation_parameters(account_number: int, amount: int) -> None:
    if not isinstance(account_number, int) and not isinstance(amount, int):
        raise NotImplementedError

def validate_deposit(account_number: int, amount: int) -> Customer:
    """Validate Deposit Transaction"""
    check_validation_parameters(account_number, amount)
    customer = get_customer(account_number)
    if customer.balance + amount > criteria.Max_Balance:
        raise errors.Max_Deposit_Balance_Error()
    if amount < criteria.Min_Deposit:
        raise errors.Min_Deposit_Error()
    if amount > criteria.Max_Deposit:
        raise errors.Max_Deposit_Error()
    if customer._no_deposit == criteria.Max_No_Deposits:
        raise errors.Max_No_Deposit_Error()
    return customer


def validate_withdrawal(account_number: int, amount: int) -> Customer:
    """Validate Withdrawal Transaction"""
    check_validation_parameters(account_number, amount)
    customer = get_customer(account_number)
    if customer.balance - amount < criteria.Min_Balance:
        raise errors.Max_Withdrawal_Balance_Error()
    if amount >= customer.balance:
        raise errors.Withdrawal_Error("Insufficient Balance")
    if amount < criteria.Min_Withdrawal:
        raise errors.Min_Withdrawal_Error()
    if amount > criteria.Max_Withdrawal:
        raise errors.Max_Withdrawal_Error()
    if customer._no_withdrawal == criteria.Max_No_Withdrawals:
        raise errors.Max_No_Withdrawal_Error()
    return customer

def validate_transfer(account_1: int, account_2: int, amount: int) -> tuple[Customer, Customer]:
    """Validate Transfer Transaction"""

    if (not isinstance(account_1, int)
        and not isinstance(account_2, int)
        and not isinstance(amount, int)):
        raise NotImplementedError

    customer_1 = get_customer(account_1)
    customer_2 = get_customer(account_2)


    if amount >= customer_1.balance:
        raise errors.Transfer_Error("Insufficient Balance")
    if customer_2.balance + amount > criteria.Max_Transfer:
        raise errors.Max_Transfer_Balance_Error()
    if amount < criteria.Min_Transfer:
        raise errors.Transfer_Error(f"Min transfer amount is {criteria.Min_Withdrawal} for account {account_1}")
    if amount > criteria.Max_Transfer:
        raise errors.Transfer_Error(f"Max transfer amount is {criteria.Max_Withdrawal} for account {account_2}")
    if customer_1._no_withdrawal == criteria.Max_No_Withdrawals:
        raise errors.Max_No_Withdrawal_Error()
    return customer_1, customer_2
