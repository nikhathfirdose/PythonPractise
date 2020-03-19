#pure function eample- compile
li = [1,2,3]
def mul(i):
  return i*2

print(list(map(mul,li)))
print(li)
#so map did the mapping but also kept the original list same, so it is a pure function coz has no "side-effects"