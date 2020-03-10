class PlayerCharacter():
  def __init__(self, name):
    self.name = name #attributes
  def run(self): #method
    print("Yayayy")
p1 = PlayerCharacter("Nikhath")
(p1.run()) #since its a method it need not print twice else like the next statement
print(p1.run()) #it will return a "None"value
print(p1.name)

