
## Table of Content

[Title and Description](https://github.com/ThakkarPurvi/Payment_Bank#payment-bank-program)

[Tech Stack](https://github.com/ThakkarPurvi/Payment_Bank#tech-stack)

[Run](https://github.com/ThakkarPurvi/Payment_Bank#run-the-program)

[Thank you](https://github.com/ThakkarPurvi/Payment_Bank#thank-you)

[Profile](https://github.com/ThakkarPurvi/Payment_Bank#-links)

# **Payment Bank Program**

A new payment bank wants to implement its banking solution. Payments banks have a 
maximum limit of ₹1,00,000 on the account balance. The balance cannot exceed this limit. The 
bank wants to put in some conditions for withdrawals and deposits to an account. Below are the 
conditions:

    ● Account balance cannot exceed ₹1,00,000
    ● Account balance cannot be less than ₹0
    ● The minimum deposit amount is ₹500 per transaction
    ● The maximum deposit amount is ₹50,000 per transaction
    ● The minimum withdrawal amount is ₹1,000 per transaction
    ● The maximum withdrawal amount is ₹25,000 per transaction
    ● No more than 3 deposits are allowed in a day
    ● No more than 3 withdrawals are allowed in a day
    ● Account number entered during deposit or withdrawal should be valid
    ● Account has sufficient balance during withdrawals

**Problem statement**

Given an input command and the necessary valid parameters, your solution should execute the 
command and return the output. Below are the commands that need to be supported along with 
description, input parameters and the expected output for each command. 
In this program, there are 8 files. 

[**bank.py**](https://github.com/ThakkarPurvi/Payment_Bank/blob/main/bank.py)

1. generate_customer_id 

2. **Class Bank** - for banking related transation

    Bank class is created for all banking transactions. This class has five methods:
        
        Have used @staticmethod decorator as staticmethod knows nothing about the class and deals with the parameters (it is bound to the class and not the object of the class).

            1. create = In the method, the system will create a new customer return account number and add the customer to a dictonary. 
            2. deposit = this method is used to deposit money in the customer's account. It takes the amount from the user and adds it to the customer_balance.
            3. balance = this method views the customer's bank balance. 
            4. withdraw = this method is used to withdraw money from the customer's account. It takes the account number and amount from the user and subtracts it from the customer_balance.
            5. transfer = this method transfers money from customer account number 1 to customer account number 2 (or vice versa). It takes the amount from the user, subtracts it from the payee's customer_balance, and adds it to the recipient account. 

[**customers.py**](https://github.com/ThakkarPurvi/Payment_Bank/blob/main/customers.py)

**Class Customer** - for customer related information

    Customer is a class for all customer-related information. 
    Once any object for this class is created, it will call the init(self) method, also known as the constructor. 
    Inside this method, we are moulding
    
        1. name as empty string
        2. account_number as empty string 
        3. balance as 0
        4. no_deposit as 0
        5. no_withdrawal as 0       
        6. no_transfers as 0
    
    str() and repr() are used to get a string representation of the object.

    Have used @property decorator to help in defining the properties.
        1. balance
        2. _deposit
        3. _withdrawal
        4. _transfer

[**criteria.py**](https://github.com/ThakkarPurvi/Payment_Bank/blob/main/criteria.py)

Programm criteiria are taken from this file.

Account Balance

    Min_Balance = 0
    Max_Balance = 100000

Deposit

    Min_Deposit = 500
    Max_Deposit = 50000
    Max_No_Deposits = 3


Withdrawal

    Min_Withdrawal = 1000
    Max_Withdrawal = 25000
    Max_No_Withdrawals = 3


Transfer

    Min_Transfer = 1000
    Max_Transfer = 25000
    Max_No_Transfers = 3

[**db.py**](https://github.com/ThakkarPurvi/Payment_Bank/blob/main/db.py)

Creates a dictionary for all the customers

[**errors.py**](https://github.com/ThakkarPurvi/Payment_Bank/blob/main/errors.py)

This file handels all the errors for Customers, Deposits, Withdrawal and Transfer.

[**validators.py**](https://github.com/ThakkarPurvi/Payment_Bank/blob/main/validators.py)

This file validates the transactions before executing Deposits, Withdrawal and Transfer.

[**main.py**](https://github.com/ThakkarPurvi/Payment_Bank/blob/main/main.py)

## Tech Stack

**Back-end**

- Python - version 3.10
    - [PyCharm](https://www.jetbrains.com/pycharm/) — to run the application 

## Run the program ##

File [main.py](https://github.com/ThakkarPurvi/Payment_Bank/blob/main/main.py)


## Thank you

**Sahaj Software**

- [Sahaj Software](https://sahaj.ai/) — for giving me this opportunity 

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/ThakkarPurvi)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thakkarpurvilondon/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/purvi41)

