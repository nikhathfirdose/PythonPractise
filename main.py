#exercise on cmprehensions

li = ["a", "b", "c", "b", "d", "n", "m", "n"]
duplicates = [c for c in li if li.count(c)>1]
chars = set(duplicates)
print("Duplicates = " , list(chars))

#decorators
from time import time

def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args, **kwargs)
    t2 = time()
    print(t2-t1)
    return result
  return wrapper

@performance
def looo():
  for i in range (10000000):
    i
looo()