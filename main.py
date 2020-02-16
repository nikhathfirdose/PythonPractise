# #5 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a1 = set(a)
b1 = set(b)
p = a1.intersection(b1)
print(p)


#6
a = input("strr: ")
b = a[::-1]
if a == b:
  print("pali")
else:
  print("lo")

#3 using list comprehensions
k =[]
l = [1,2,4,5,67,77,89,9]
k = [i for i in l if i<5]
print(k)

#7
a= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
j = [i for i in a if i%2==0]
print(j)

#8
u1 = input("move1 ")
u2 = input("move2 ")

if (u1 == "r" and u2 == "s") or (u1 == "p" and u2 == "r") or (u1 == "s" and u2 == "p"):
  print("u1 won")
elif u1 ==u2:
  print("its a draw")
else:
  print("u2 won")

#9
import random
k = random.randint(2,3)
u = int(input("enter number: "))
if(abs(u-k)==0):
  print("bingo! you guessed it right")
elif abs(u-k) <=2 :
  print("close")
else:
  print("too farr")
print("the random number was",k)

#9 till exit
import random

number = random.randint(1,9)
guess = 0
count = 0


while guess != number and guess != "exit":
    guess = input("What's your guess?")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")



#10
a = []
s = int(input("list length of a "))
for i in range (s):
  data = int(input(f"value of index{i} ="))
  a.append(data)
b = []
h = int(input("list length of b "))
for i in range (h):
  dat = int(input(f"value of index{i} ="))
  b.append(dat)
a2 = set(a)
b2 = set(b)
k = a2.intersection(b2)
print("intersection is ",list(k))
