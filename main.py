#Inheritance

class User:
  def sign():
    return "Hi You're signed in"
    
class Wizard(User):
  def log():
    return "Login Now"
  

class Archer(Wizard):
  pass

w1 = Archer.sign()
print(w1)  #as archer inherits wizard which inherits user that has the sign method. it still works on Archer

#this totatlly works. Awesome!