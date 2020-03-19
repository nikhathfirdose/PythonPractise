#pure function eample

def mulby2(li):
  nli =[] 
  for item in li:
    nli.append(item*2)
  return nli
nli = "" #this affects if nli is in the outside scope, but has no affect if nli is paced inside
print(mulby2([1,2,3]))