#Exercise Cat 2nd Time

class Cat:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  
  def Oldest(*args):
    return max(args)

c1 = Cat("pp", 8)
c2 = Cat('oo',8)
c3 = Cat("poil", 9)

print(f'the oldest is {Cat.Oldest(c1.age,c2.age,c3.age)} years old')