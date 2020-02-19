def highestEven(li):
  even = []
  for i in li:
    if i%2 == 0:
      even.append(i)
  return max(even)

print(highestEven([1,2,3,45,-7,5,6,7778,8]))

#Exercise find highest even number




