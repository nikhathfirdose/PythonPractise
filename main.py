#classes

class Player:
  member = True #class object attribute (static)
  def __init__(self,n):
    self.n = n #attributes (dynamic)
  def run(self):#method
    print("kk")

p1 = Player("Nikhath")
print(p1.n)
(p1.run())