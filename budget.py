class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0

  def deposit(self, amount, description = ""):
    #apped to ledger
    self.ledger.append({
      "amount": amount,
      "description": description,
      })
  
  def withdraw(self, amount, description = ""):
    if not self.check_funds(amount):
            return False
  
    self.balance -= amount
    self.ledger.append({
      'amount': -amount,
      'description': description,
      })

    return True

  def get_balance(self):
    return self.balance
    
  def transfer(self, amount, destination):
    self.balance -= amount
    destination.balance += amount
    #print("Transfer to [Destination Budget Category]")
  

  def check_funds(self, amount):
    if self.balance < amount:
        return False
    return True
    
  
  
 



def create_spend_chart(categories):