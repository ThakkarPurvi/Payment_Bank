from . import criteria

"""Invalid Customer Error"""

class Invalid_Customer_Error(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

""" Deposit Errors"""

class Deposit_Error(Exception):
    def __init__(self,  message: str) -> None:
        super().__init__(message)

class Min_Deposit_Error(Deposit_Error):
    def __init__(self) -> None:
        super().__init__(f"Min Deposit amount is {criteria.Min_Deposit}")

class Max_Deposit_Error(Deposit_Error):
    def __init__(self) -> None:
        super().__init__(f"Max Deposit amount is {criteria.Max_Deposit}")

class Max_Deposit_Balance_Error(Deposit_Error):
    def __init__(self) -> None:
        super().__init__(f"Max Deposit balance exceeded")

class Max_No_Deposit_Error(Deposit_Error):
    def __init__(self) -> None:
        super().__init__(f"No more than 3 transactions are allowed in a day")

""" Withdrawal Errors"""

class Withdrawal_Error(Exception):
    def __init__(self,  message: str) -> None:
        super().__init__(message)

class Min_Withdrawal_Error(Withdrawal_Error):
    def __init__(self) -> None:
        super().__init__(f"Min Withdrawal amount is {criteria.Min_Withdrawal}")

class Max_Withdrawal_Error(Withdrawal_Error):
    def __init__(self) -> None:
        super().__init__(f"Max Withdrawal amount is {criteria.Max_Withdrawal}")

class Max_Withdrawal_Balance_Error(Withdrawal_Error):
    def __init__(self) -> None:
        super().__init__(f"Max Withdrawal balance exceeded")

class Max_No_Withdrawal_Error(Withdrawal_Error):
    def __init__(self) -> None:
        super().__init__(f"No more than 3 transactions are allowed in a day")

""" Transfer Errors"""

class Transfer_Error(Exception):
    def __init__(self,  message: str) -> None:
        super().__init__(message)

class Min_Transfer_Error(Transfer_Error):
    def __init__(self) -> None:
        super().__init__(f"Min Transfer amount is {criteria.Min_Withdrawal}")

class Max_Transfer_Error(Transfer_Error):
    def __init__(self) -> None:
        super().__init__(f"Max Transfer amount is {criteria.Max_Withdrawal}")

class Max_Transfer_Balance_Error(Transfer_Error):
    def __init__(self) -> None:
        super().__init__(f"Max Transfer balance exceeded")

class Max_No_Transfers_Error(Transfer_Error):
    def __init__(self) -> None:
        super().__init__(f"No more than 3 transfers are allowed in a day")


