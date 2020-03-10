class Player:
  #class Attribute
  member = True 
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def run(self):
    return "my name is" + self.name # return use "+" forrint use ","

p1 = Player("cindy", 6)
p2 = Player("raj", 56)
print(p2.run())  #these both change == Dynamic
print(p1.run()) 
print(p1.member) #always true == Static

