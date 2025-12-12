class BankAccount:
  def __init__(self):
    self.__balance=0
  def deposite(self,amount):
    self.__balance=amount+self.__balance
    print(f"You has deposited {amount} birr and Your current balance is {self.__balance}")
  def withdraw(self,amount):
    if amount<=self.__balance:
        self.__balance=self.__balance-amount
        print(f"Your account has been debited with {amount} birr and your current balance is {self.__balance}")
    else:
      print("Insufficient balance")
  def get_balance(self):
    return self.__balance
account1=BankAccount()
while True:
 print("____MENU_____")
 print("1.Deposite\n2.Withdraw\n3.Get balance\n4.Exit\n")
 c=int(input("enter your choice"))
 if c==1:
  Amount1=float(input("Enter the amount of money"))
  account1.deposite(Amount1)
 elif c==2:
  Amount2=float(input("Enter the amount of money"))
  account1.withdraw(Amount2)
 elif c==3:
  b=account1.get_balance()
  print(f"Your current balance is {b} birr")
 elif c==4:
   print("Goodbye!")
   break
 else:
  print("Invalid choice")
 


    