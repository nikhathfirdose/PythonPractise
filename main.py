#squares
my_ist = [5,4,3]
print(list(map(lambda i:i **2, my_ist)))


#list sort
a= [(0,2), (4,1), (9,9), (10, -1)]
a.sort(key=lambda i: i[1])
print(a) 