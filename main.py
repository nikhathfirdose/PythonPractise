# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
      print(args[0]['name']) #[0] gives the first argument user1
      res =fn(*args, **kwargs)
      return res
  return wrapper



@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
 # A grocery shop gives discount of 10% on a particular product if the cost of the quantity purchased crosses 1000.  The price of one piece of this product is Rs. 100. Write an algorithm to calculate the price a person will have to pay, given the quantity he purchase

def Dicount(amt):
  if amt>=1000:
    percent = 10/100
    totalpay = amt-(amt*(percent))
  else:
    totalpay = "no discount"
  return totalpay
print(Dicount(9000))

# A computer teacher wants his students to find the number of days in the month of February depending on whether it is a leap year or not. Build an algorithm for the same.

def leap(year):
  if year%4==0:
    if year%100==0 and year%400==0:
        days = 29
    else:
      days= 28
  else:
    days = 29
  return days

print(leap(1900))

#count of a number

def coun(num, digit):
  c=0
  while(num>0):
    if num%10 == digit:
      c=c+1
    num =int(num/10)
  return c

print(coun(12222456666, 2))

#count using built infunction

# n = (input())
# d = (input())
# print(n.count(d))




#priime factpr

# def factor(number):
#   li =[]
#   p =[]
#   for i in range(1,number+1):
#     if number%i ==0:
#       li.append(i)
#   for n in li:
#     if n>1:
#       for i in range(2,number):
#         if n%i==0:
#           p.append(n)
#   return p
def check_prime(number):
  if number>1:
    for i in range(2,number):
      if number%i==0:
        return False
        break
    else:
      return True
  else:
    return False

def factor(number):
  li =[]
  p =[]
  for i in range(1,number+1):
    if number%i ==0:
      li.append(i)
  for j in li:
    if check_prime(j):
      p.append(j)
  return p
#nothing
print(factor(600))
print(factor(600))
