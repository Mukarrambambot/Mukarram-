class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      return f"Deposited ${amount}. New balance is ${self.__account_balance}."
    else:
      return "Invalid deposit amount."

  def withdraw(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      return f"Withdrew ${amount}. New balance is ${self.__account_balance}."
    else:
      return "Invalid withdrawal amount."

  def display_balance(self):
    return f"Account balance for {self.__account_holder_name} is ${self.__account_balance}."


# Example usage with user input:
if __name__ == "__main":
  account_number = input("Enter account number: ")
  account_holder_name = input("Enter account holder name: ")
  initial_balance = float(input("Enter initial balance: "))

  account = BankAccount(account_number, account_holder_name, initial_balance)

  print(account.display_balance())

  while True:
    print("\n1. Deposit\n2. Withdraw\n3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
      amount = float(input("Enter the deposit amount: "))
      print(account.deposit(amount))
    elif choice == "2":
      amount = float(input("Enter the withdrawal amount: "))
      print(account.withdraw(amount))
    elif choice == "3":
      print("Thank you for using our banking system!")
      break
    else:
      print("Invalid choice. Please select 1, 2, or 3.")
