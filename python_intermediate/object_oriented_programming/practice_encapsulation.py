class BankAccount():
  
  def __init__(self):
    self.money = 100000 #cashback
    self.__deposit = 0
  
  def get_deposit(self):
    return self.__deposit
  
  def set_deposit(self, add_deposit):
    self.__deposit += add_deposit


bank_saras = BankAccount()
print(bank_saras.money)

# print(bank_saras.__deposit)

print(bank_saras.get_deposit())

bank_saras.set_deposit(200000)

print(bank_saras.get_deposit())