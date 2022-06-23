from PaymentBank.db import customers
from PaymentBank.bank import Bank

cus1 = Bank.create("Amit Dugal")
cus2 = Bank.create("Gauri Kalla")
cus3 = Bank.create("Phani Kumar")
cus4 = Bank.create("Veda Kanala")

print(customers)

Bank.deposit(cus1, 50000)
# Bank.deposit(cus1, 1000)


# Bank.withdraw(cus1, 1000)
# Bank.withdraw(cus1, 1000)
# Bank.withdraw(cus1, 2000)

Bank.transfer(cus1, cus2, 1000)
Bank.transfer(cus1, cus3, 10000)
Bank.transfer(cus1, cus4, 5000)
# Bank.transfer(cus1, cus2, 1000)

Bank.balance(cus1)
Bank.balance(cus2)
Bank.balance(cus3)
Bank.balance(cus4)

