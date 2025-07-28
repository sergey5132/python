# Банкир.

# Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.

# Напишите тут ваш код

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            print("ammount can not be negative")
        else:
            self.initial_balance += amount
            print(f"Current balance = {self.initial_balance}")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.initial_balance:
            print("can not withdraw")
        else:
            self.initial_balance -= amount
            print(f"Current balance = {self.initial_balance}")


b = BankAccount(1, 10)

b.deposit(10)
b.withdraw(5)
b.withdraw(4)

