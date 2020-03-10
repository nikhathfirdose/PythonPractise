#Polymorphism

class User:
  def sign():
    return "hoolaaa"
class Wizard(User):
  def __init__(self, name):
    self.name= name

  def attack(self):
    print(f'with wizard arrows {self.name}')


class Archer(User):
  def __init__(self, name):
    self.name= name

  def attack(self):
    print(f'with archer arrows {self.name}')

w1 = Wizard("Noonn")
a1 = Archer("lol")
#1st method to call the attacks
w1.attack()
a1.attack()

#2nd method
def use_attack(c):
  c.attack()
use_attack(w1)
use_attack(a1)

#3rd method
for c in [w1, a1]:
  c.attack()