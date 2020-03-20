#list comprehensions
li = [i for i in range(0,100) if i%2==0]
print(li)

#set - same as lists
si = { i for i in [1,2,3,3,6,33,4]}
print(si)

#dict comprehensions
sample = {
  "a":5,
  "b": 6
}
new_d = {k:v**2 for k,v in sample.items()}
print(new_d)


#dict copre hension by just using key
dics = { k: k*2 for k in [1,2,3]}
print(dics)