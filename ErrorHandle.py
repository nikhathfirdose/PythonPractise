#Error Handling

while (True):
    try:
        a = int(input("age?"))
        (10/a)
    except ValueError:
        print("enter a number")
    except ZeroDivisionError:
        print("It cannot be zero! Try again")
    else:
        print(f'youre age is {a}')
        break
    finally:
        print("hi user! :)")
