class chair:
    def _init_ (self ,color, material, size)
    self,color= color
    self, material = material
    self,size = size


    def light (self):
          print("The chair is moving")

    def describe(self):
         print("The chair is made with (self,material) ")

#Create multiple instances using the class "chair"
 #Instance 1
Chair1= chair(green,plastic,2*2)
#Instance 2
Chair2 = chair(black,wood,2*6)

print(chair,material)
print(chair,material)
chair1,describe()
chair2,describe()

class BankAccount:
    def __init__(self, holder: str, initial_balance: float):
        self.holder = holder
        self.__balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            print(f"[{self.holder}] Deposit failed: Amount must be greater than zero.")
            return
        
        self.__balance += amount
        print(f"[{self.holder}] Successfully deposited ${amount:,.2f}.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print(f"[{self.holder}] Withdrawal failed: Amount must be greater than zero.")
            return
        if amount > self.__balance:
            print(f"[{self.holder}] Withdrawal failed: Insufficient funds. Available balance: ${self.__balance:,.2f}.")
            return
        
        self.__balance -= amount
        print(f"[{self.holder}] Successfully withdrew ${amount:,.2f}.")

    def check_balance(self):
        print(f"[{self.holder}] Current Balance: ${self.__balance:,.2f}")
        return self.__balance

account_raul = BankAccount("Raúl Pérez", 5000.0)
account_joel = BankAccount("Joel López", 3000.0)




# Account 1: Raúl Pérez
print("--- Account 1 Actions ---")
print(f"Account Holder: {account_raul.holder}")
account_raul.check_balance()
account_raul.deposit(1200.0)
account_raul.withdraw(500.0)
account_raul.check_balance()

print("\n--- Account 2 Actions ---")
# Account 2: Joel López
print(f"Account Holder: {account_joel.holder}")
account_joel.check_balance()
account_joel.deposit(500.0)
account_joel.withdraw(1000.0)
account_joel.check_balance()





