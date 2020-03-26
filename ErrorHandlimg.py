#Error Handling
while(True):
  try:
    a = int(input("age?"))
    print(a)
  except ValueError:
    print("enter a number")
  except ZeroDivisionError:
    print("It cannot be zero! Try again")
  else:
    print(f'you\'re age is {a}')
    break
