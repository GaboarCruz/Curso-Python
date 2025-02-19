class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

person1 = Person("Ana", 30)
person2 = Person("Gabriel", 24)

# person1.greet()
# person2.greet()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ah depositado: {amount}. Saldo actual {self.balance:.2f}")
        else:
            print("No se puede depositar dinero, cuenta desactivada")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado: {amount}. Saldo actual {self.balance:.2f}")
            else: 
                print("No cuenta con suficientes montos")
        else:
            print("No puede retirar, su cuenta esta desactivada")

    def deactive_account(self):
        self.is_active = False
        print("La cuenta ah sido desactivada")

    def activate_account(self):
        self.is_active = True
        print("La cuenta ah sido activada")

cuenta1 = BankAccount("Gabo", 250.42)
cuenta1.deposit(40)
cuenta1.withdraw(200)
cuenta1.deactive_account()
cuenta1.withdraw(200)
cuenta1.activate_account()
cuenta1.withdraw(200)