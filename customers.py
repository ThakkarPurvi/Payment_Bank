class Customer:
    def __init__(self, name: str, account_number: int):
        self.name = name
        self.account_number = account_number
        self._account_balance = 0
        self._no_deposit = 0
        self._no_withdrawal = 0
        self._no_transfers = 0

    def __repr__(self) -> str:
        return f"Customer Name: {self.name}, Account No: {self.account_number}\n"

    def __str__(self) -> str:
        return f"Customer Name: {self.name}, Account No: {self.account_number}"

    @property
    def balance(self) -> int:
        """Account Balance"""
        return self._account_balance

    def _deposit(self, amount: int) -> None:
        """Deposit"""
        self._account_balance += amount
        self._no_deposit += 1

    def _withdrawal(self, amount: int) -> None:
        """Withdrawal"""
        self._account_balance -= amount
        self._no_withdrawal += 1

    def _transfer(self) -> None:
        """No of Transfers"""
        self._no_transfers += 1

