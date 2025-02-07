class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Счет пополнен на {amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма для пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Со счета снято {amount}. Новый баланс: {self.balance}")
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Сумма для снятия должна быть положительной.")

    def __str__(self):
        return f"Баланс: {self.balance}"


account = BankAccount(1000)

print(account)

account.deposit(500)

account.withdraw(200)

account.withdraw(2000)

print(account)